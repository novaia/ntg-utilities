## Upload folder to GCS bucket
```
gcloud cp -r C:/Users/Hayden/Desktop/heightmaps/uncorrupted_split_heightmaps gs://cloud-ai-platform-a013866a-a18a-470f-9d35-f485abb17e82
```

## Move folder from GCS bucket to Vertex AI notebook
```
gutil -m cp -r gs://cloud-ai-platform-a013866a-a18a-470f-9d35-f485abb17e82/uncorrupted_split_heightmaps/ /home/jupyter/
```

## Mount GCS bucket to Vertex AI notebook
[reference](https://cloud.google.com/blog/topics/developers-practitioners/cloud-storage-file-system-vertex-ai-workbench-notebooks)
```
MY_BUCKET=cloud-ai-platform-a013866a-a18a-470f-9d35-f485abb17e82

cd ~/

mkdir -p gcs

gcsfuse --implicit-dirs --rename-dir-limit=100 --disable-http2 --max-conns-per-host=100 $MY_BUCKET "/home/jupyter/gcs"
```
