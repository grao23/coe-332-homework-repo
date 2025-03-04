FROM python:3.12

RUN pip3 install xmltodict
RUN pip3 install datetime
RUN pip3 install pandas
RUN pip3 install pytest==8.3.4
RUN pip3 install flask
RUN pip3 install requests


RUN mkdir /app
WORKDIR /app


COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt


COPY iss_tracker.py /app/iss_tracker.py
COPY test_iss_tracker.py /app/test_iss_tracker.py



RUN chmod +rx /app/iss_tracker.py
RUN chmod +rx /app/test_iss_tracker.py



ENV PATH="/app:$PATH"


ENTRYPOINT ["python"]

CMD ["iss_tracker.py"]
CMD ["test_iss_tracker.py"]
