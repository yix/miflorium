ARG ARCH=
FROM ${ARCH}python:3.6.10-alpine3.11 as builder
# requires --cap-add=NET_ADMIN to docker run
WORKDIR /build
COPY requirements.txt .
RUN apk --no-cache add alpine-sdk glib-dev && pip wheel -r requirements.txt

FROM ${ARCH}python:3.6.10-alpine3.11

WORKDIR /app
COPY --from=builder /build/*.whl ./
COPY --from=builder /usr/lib/libglib-2.0.so.0 /usr/lib/libpcre.so.1 /usr/lib/
RUN pip install *.whl
COPY miflorium.py ./

USER nobody
ENTRYPOINT ["/usr/local/bin/python", "miflorium.py"]
CMD ["--scan"]
# --scan requires --user=root to docker run

