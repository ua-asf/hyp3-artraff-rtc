"""artraff-rtc processing for HyP3."""

import logging
from argparse import ArgumentParser

from hyp3lib.aws import upload_file_to_s3

from hyp3_artraff_rtc.process import process_artraff_rtc


def main() -> None:
    """HyP3 entrypoint for hyp3_artraff_rtc."""
    parser = ArgumentParser()
    parser.add_argument('--bucket', help='AWS S3 bucket HyP3 for upload the final product(s)')
    parser.add_argument('--bucket-prefix', default='', help='Add a bucket prefix to product(s)')

    # RTC arguments
    parser.add_argument('patform', help='Platform to create RTC for')
    parser.add_argument('granule', help='Data granule to create an RTC for.')
    parser.add_argument('--dem', default=None, help='Path to the DEM to use for processing')
    parser.add_argument('--resolution', type=float, default=3.0, help='Resolution of the output RTC (m)')
    parser.add_argument('--work-dir', default='/tmp/work', help='Working directory for processing')

    args = parser.parse_args()

    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO
    )

    product_file = process_artraff_rtc(
        greeting=args.greeting,
    )

    if args.bucket:
        upload_file_to_s3(product_file, args.bucket, args.bucket_prefix)


if __name__ == '__main__':
    main()
