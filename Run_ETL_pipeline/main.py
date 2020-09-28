
import apache_beam as beam
from apache_beam.io import ReadFromText
from apache_beam.io import WriteToText
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import SetupOptions

import logging
import argparse
from datetime import datetime


class FilteringSales(beam.DoFn):
  def process(self, element, lower_bound):
    d = datetime.strptime(element['date'], '%Y-%m-%d')

    #filter by date
    if d > lower_bound:
      yield element
    else:
      return

def run(argv=None, save_main_session=True):
  parser = argparse.ArgumentParser()
  parser.add_argument(
      '--temp_location',
      dest='temp_location',
      help='temp_location path.')
  known_args, _ = parser.parse_known_args(argv)

  with beam.Pipeline() as p:
    sellers = p | 'Read Sellers' >> beam.io.ReadFromParquet('data/sellers_parquet/*.parquet')
    sales = p | 'Read Sales' >> beam.io.ReadFromParquet('data/sales_parquet/*.parquet')

    #filter by seller_id
    filtered_sales = sales | beam.Filter(lambda x: x['seller_id'] in ['1', '2']) | beam.ParDo(FilteringSales(), datetime.strptime('2020-01-01', '%Y-%m-%d'))
    filtered_sales | beam.Map(print)

    table_schema = 'product_id:STRING, order_id:STRING, seller_id:STRING, date:STRING, num_pieces_sold:STRING, bill_raw_text:STRING'
    table_spec = 'refined-lotus-290713:first_database.orders'

    filtered_sales | beam.io.WriteToBigQuery(
	    table_spec,
	    schema=table_schema,
      custom_gcs_temp_location= known_args.temp_location,
	    write_disposition=beam.io.BigQueryDisposition.WRITE_TRUNCATE,
	    create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED)


if __name__ == '__main__':
  logging.getLogger().setLevel(logging.INFO)
  run()