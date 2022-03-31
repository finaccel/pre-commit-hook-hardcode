import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*")
    args = parser.parse_args()
        
    errors      = []
    count_lines = 0
    for filename in args.filenames:
        with open(filename, 'rb') as fb:  
            for line in fb:
                sens = line.decode()
                for word in sentences['data']:
                    if word in sens:
                        errors.append(TypeError(f"{filename} have hardcode ({word}%) line:{count_lines}"))
                count_lines += 1
    
    if len(errors) > 0:
        return errors
    
    return 0

sentences = {
    "data":[
        "kre-data-warehouse-prod-6615",
        "kre-data-warehouse-stg-ccbf",
        "kre-gcs-kredivo-etl-prod",
        "asia-southeast1-kre-data-kr-7c044bae-bucket",
        "dwh-etl-kredivo",
        "kre-gcs-kredifazz-etl-prod",
        "asia-southeast1-kre-data-kd-08201529-bucket",
        "dwh-etl-kredifazz",
        "kre-gcs-blpl-etl-prod",
        "asia-southeast1-kre-data-bl-9bf559d6-bucket",
        "dwh-etl-blpl",
        "dwh-etl-vietnam",
        "dwh-etl-halokas",
        "dwh-etl-efishery",
        "asia-northeast1",
        "gs://asia-northeast1-kre-compose-01f4bf4d-bucket/dags",
        "asia-northeast1-kre-compose-01f4bf4d-bucket",
        "/home/airflow/gcs/plugins/",
        "asia-southeast2",
        "asia-southeast2-a",
        "kre-dataproc-etl-prod",
        "gs://kre-gcs-kredivo-etl-prod",
        "gs://kre-gcs-kredivo-etl-prod/data",
        "gs://kre-dataproc-etl-prod-temp",
        "kre-dataproc-etl-prod-temp",
        "gs://kre-gcs-kredifazz-etl-prod",
        "gs://kre-gcs-kredifazz-etl-prod/data",
        "gs://kre-dataproc-etl-kredifazz-prod-temp",
        "kre-dataproc-etl-kredifazz-prod-temp",
        "gs://kre-gcs-blpl-etl-prod ",
        "kre-gcs-blpl-etl-prod ",
        "gs://kre-gcs-blpl-etl-prod/data",
        "gs://kre-dataproc-etl-blpl-prod-temp ",
        "kre-dataproc-etl-blpl-prod-temp",
        "fpl-dwhs-etl-prd-cce-apse1-shared-bc22",
        "kre-composer-cdc-prod",
        "kre-composer-etl-prod",
        "kre-composer-etl-prod-rev-01",
        "kre-composer-mle-prod",
        "kre-data-blpl-etl-prd-cce-apse1",
        "kre-data-cdc-etl-prd-cce-apse1",
        "kre-data-kdfz-etl-prd-cce-apse1",
        "kre-data-krdv-etl-prd-cce-apse1",
        "/home/airflow/gcs",
        "/home/airflow/gcs/dags"
    ]    
}

if __name__ == "__main__":
    main()