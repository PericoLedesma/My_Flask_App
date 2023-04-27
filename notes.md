flask : microweb framework

falsk vs django
less tools than django


https://www.youtube.com/watch?v=mqhxxeeTbu0

We are using Jinga to use template language - jinga . It lets us write pythion in html without using javascript template html templates

the good think of jinga templates we can pass variables to the templates
        return render_template('login.html', text='Testing')


{{ text }} <- to use the variable in html by using python

bootstrap

````
docker build \
--build-arg REACT_APP_BACKEND_URL="https://4567-$GITPOD_WORKSPACE_ID.$GITPOD_WORKSPACE_CLUSTER_HOST" \
--build-arg REACT_APP_AWS_PROJECT_REGION="$AWS_DEFAULT_REGION" \
--build-arg REACT_APP_AWS_COGNITO_REGION="$AWS_DEFAULT_REGION" \
--build-arg REACT_APP_AWS_USER_POOLS_ID=“eu-central-1_m6hu1cbSu" \
--build-arg REACT_APP_CLIENT_ID="6h42orvqfbgku4g88q0lnjou1u" \
-t frontend-react-js \
-f Dockerfile.prod \
.
````

