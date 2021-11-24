
#### Build your container </br>
docker image build -t mymlapp </br>
#### Run your container</br>
docker run -it 80:8000 mymlapp</br>
80 is the port of the host, 8000 is the port of the guest(in this case docker container)</br>


for no-cache dir discussion: https://stackoverflow.com/questions/45594707/what-is-pips-no-cache-dir-good-for</br>
# Tag image to push docker hub and push </br>
docker tag mymlapp themeansquare/mymlapp</br>
docker push themeansquare/mymlapp</br>
-> create kubernetes cluster</br>
#### To see clusters on CLI</br>
gcloud container clusters list</br>
#### To set default cluster on CLI</br>
gcloud config set container/cluster cluster-1</br>
#### Connect cluster</br>
gcloud container clusters get-credentials cluster-1 --zone us-central1-c --project hardy-baton-332508</br>
#### Deploy the container to your cluster</br>
kubeclt apply -f build.yaml</br>
#### See your pod in the workloads. From actions, expose your pod via load balancer.</br>
