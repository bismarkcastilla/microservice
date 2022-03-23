FROM python:3.9-slim-buster

RUN adduser worker
USER worker
WORKDIR /home/worker

COPY --chown=worker:worker requirements.txt requirements.txt
RUN pip3 install --user -r requirements.txt

ENV PATH="/home/worker/.local/bin:${PATH}"

COPY --chown=worker:worker . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
