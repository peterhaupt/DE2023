gsutil cp ../lab4/data/* gs://data_de2023_peterhaupt

git config --global user.email "indika@example.com"
git config --global user.name "Indika Kumara"
echo "data uploaded" >> ct_pipeline/history.txt
git commit -am "data uploaded"
git push https://$1:$2@github.com/peterhaupt/DE2023.git --all

