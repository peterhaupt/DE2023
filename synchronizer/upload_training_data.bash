gsutil cp ../lab2/data/* gs://data-de2023


echo 'data uploaded' >> ct_pipeline/history.txt
git commit -am “data uploaded”
git git push https://$1:$2@github.com/IndikaKuma/DE2023.git --all
