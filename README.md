

docker image build -t mymlapp
docker run -it 80:8000 mymlapp
80 is the port of the host, 8000 is the port of the guest(in this case docker container)


for no-cache dir discussion: https://stackoverflow.com/questions/45594707/what-is-pips-no-cache-dir-good-for

docker tag mymlapp themeansquare/mymlapp
docker push themeansquare/mymlapp
-> create kubernetes cluster
#### To see clusters on CLI
gcloud container clusters list
#### To set default cluster on CLI
gcloud config set container/cluster cluster-1
#### Connect cluster
gcloud container clusters get-credentials cluster-1 --zone us-central1-c --project hardy-baton-332508