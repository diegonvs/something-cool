## I've made this app to pratice some docker tutorials

### To execute this beautiful app is *NEEDED* get a alpine container :heart:

```
$ docker image pull alpine
```

### So, we can build the image using:

```
$ docker image build -t <YOUR_USERNAME>/nameapp .

```

### If build is successful we can finally run using:

```
$ docker container run -p 8888:5000 --name nameapp <YOUR_USERNAME>/nameapp

```

:fire:
