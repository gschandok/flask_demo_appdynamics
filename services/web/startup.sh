#!/bin/bash

echo "Inside startup.sh file"

if [ "${APPDYNAMICS_ENABLED}" = "true" ]; then
  if [ -z "${AGENT_VERSION}" ]; then
    echo "installing appdynamics"
    pip install -U --default-timeout=1000 appdynamics || exit $?
  else
    pip install -U appdynamics==${AGENT_VERSION} || exit $?
  fi
  # start app
  echo "starting server with appdynamics monitoring"
  pyagent run -c appdynamics.cfg - gunicorn -w 4 -b 0.0.0.0:5000 manage:app
else
  gunicorn -w 4 -b 0.0.0.0:5000 manage:app
fi

# init db
flask db init
flask db migrate
flask db upgrade