# ------------------------------------------------------------------------------
# Base

FROM golang:1.20.2-alpine

SHELL ["/bin/ash", "-c"]

# ------------------------------------------------------------------------------
# Working directory

RUN set -exo pipefail                   && \
                                           \
    echo 'Create the working directory' && \
    mkdir /work

WORKDIR /work

# ------------------------------------------------------------------------------
# Packages

RUN set -exo pipefail                 && \
                                         \
    echo 'Installing common packages' && \
    apk add --update --no-cache \
      build-base                \
      ca-certificates           \
      curl                      \
      git                       \
      libc6-compat              \
      libstdc++                 \
      make                      \
      rsync                     \
      npm                             && \
    npm install --global http-server



# ------------------------------------------------------------------------------
# Hugo

RUN set -exo pipefail                                                    && \
                                                                            \
    echo 'Seting up temporary environment variables'                     && \
    VERSION=0.111.3                                                      && \
    SHA=b6eeb13d9ed2e5d5c6895bae56480bf0fec24a564ad9d17c90ede14a7b240999 && \
    PACKAGE=hugo-"$VERSION".tar.gz                                       && \
    BASE=https://codeload.github.com/gohugoio/hugo/tar.gz/refs/tags      && \
    URL="$BASE/v$VERSION"                                                && \
                                                                            \
    echo 'Downloading Hugo'                                              && \
    curl -fsSLo "$PACKAGE" "$URL"                                        && \
                                                                            \
    echo 'Checking package signature'                                    && \
    sha256sum "$PACKAGE"                                                 && \
    echo "$SHA  $PACKAGE" | sha256sum -c -                               && \
                                                                            \
    echo 'Extracting package'                                            && \
    mkdir -p /var/hugo                                                   && \
    tar -xzf "$PACKAGE" -C /var/hugo --strip-components=1                && \
    rm -rf "$PACKAGE"                                                    && \
                                                                            \
    echo 'Compile Hugo'                                                  && \
    cd /var/hugo                                                         && \
    CGO_ENABLED=1                                                           \
    GOPATH=/var/hugo/gopath                                                 \
    go build -v -o bin/hugo --tags extended -gcflags="-e"                && \
    mv bin/hugo /usr/local/bin/                                          && \
    rm -rf /var/hugo ~/.cache ~/go

# ------------------------------------------------------------------------------
# Copy files
COPY .git /app/.git
COPY ./docs /app/docs

RUN cd /app/docs \
    && npm install

# ------------------------------------------------------------------------------
# Execution
WORKDIR /app/docs
EXPOSE 8080

RUN /usr/local/bin/hugo

WORKDIR /app/docs

CMD ["http-server", "public"]
