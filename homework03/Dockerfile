FROM python:3.12

RUN pip3 install pytest==8.3.4

COPY ml_data_analysis.py /code/ml_data_analysis.py
COPY test_ml_data_anaysis.py /code/test_ml_data_analysis.py
COPY gcd_algorithm.py /code/gcd_algorithm.py
COPY gcd_algorithm.py /code/test_gcd_algorithm.py

RUN chmod +rx /code/ml_data_analysis.py
RUN chmod +rx /code/test_ml_data_analysis.py
RUN chmod +rx /code/gcd_algorithm.py
RUN chmod +rx /code/test_gcd_algorithm.py

ENV PATH="/code:$PATH"



