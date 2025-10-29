FROM gcr.io/google.com/cloudsdktool/google-cloud-cli:slim
WORKDIR /app
COPY runner.sh .
ENV REGION="" PROJECT_ID=""
ENTRYPOINT ["/bin/bash","/app/runner.sh"]
