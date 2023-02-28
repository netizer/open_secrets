# Open Secrets

This library is used for dealing with secrets (the ones usually kept in environment variables) in 2 environments: Google Cloud and local.

Google Cloud has a service for storying secrets - Secret Manager.
It is convenient to have local-environment counterparts of these secrets. These local versions could be viewed as mocks, e.g. we can start a couple of services locally, and use `localhost` with a couple of different ports instead of the URLs of the deployed services.

This library is very simple. It uses Google Cloud's Secret Manager whenever there is a `GOOGLE_CLOUD_PROJECT` environment variable available, and `env_vars.yaml` in the project directory otherwise.

Storing local counterparts of secrets in a YAML file is better than keeping them in environment variables because:
1. We can see which secrets does the application depend on. Environment variables are shared between applications, so it's not easy to see which ones belong to one specific application.
2. Adding a new secret means its automatic distribution among all the people using the same git repository.

## Plans forward

The library is meant to be very simple, but there is one aspect that would be very useful and I will introduce it as soon as I need it - local secrets outside of git.

Sometimes the local counterpart of a secret is not so public. Let's say we use an external service, and we have one instance of it to be used in testing, and we choose to use it from the local environment.

We still want to distribute the information that the new secret was introduced, but we don't want the actual secret to be checked into the git repository.

Currently I plan to implement it as follows:
* There will be another file `secret_env_vars.yaml` that should be added to `.gitignore` of the project that uses `open_secrets`
* If we want to add a new secret there, we should still add an entry to the `env_var.yaml` but the entry should be an array and should look like this:
```
  SOME_SECRET:
    - SECRET_ENV_VAR
    - v1
```
* The number at the end is a version number. We should now add another entry to the `secret_env_var.yaml` that looks like this:
```
  SOME_SECRET:
    v1: some value
```

This way, we can always add new versions of variables, ad if we will miss them in the `secret_env_var.yaml` we will know that we need to ask the person that added that version to `env_var.yaml` for the actual valua of the local counterpart of the secret.
