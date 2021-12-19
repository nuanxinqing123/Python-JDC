FROM python:3.7

WORKDIR /usr/src/app

COPY . .
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --no-cache-dir -r requirements.txt

CMD ["yum install mesa-libGL.x86_64"]
CMD ["python", "app.py"]