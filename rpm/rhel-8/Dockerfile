ARG GO_IMAGE
ARG DISTRO=rhel
ARG SUITE=8
ARG BUILD_IMAGE=dockereng/${DISTRO}:${SUITE}-s390x

FROM ${GO_IMAGE} AS golang

FROM ${BUILD_IMAGE}
ENV GOPROXY=direct
ENV GO111MODULE=off
ENV GOPATH=/go
ENV PATH $PATH:/usr/local/go/bin:$GOPATH/bin
ENV AUTO_GOPATH 1
ENV DOCKER_BUILDTAGS seccomp selinux exclude_graphdriver_btrfs
ENV RUNC_BUILDTAGS seccomp selinux
ARG DISTRO
ARG SUITE
ENV DISTRO=${DISTRO}
ENV SUITE=${SUITE}
ENV CC=gcc

RUN yum install -y rpm-build rpmlint libarchive yum-utils
COPY SPECS /root/rpmbuild/SPECS

# TODO change once we support scan-plugin on other architectures
RUN \
  if [ "$(uname -m)" = "x86_64" ]; then \
    yum-builddep -y /root/rpmbuild/SPECS/*.spec; \
  else \
    yum-builddep --define '_without_btrfs 1' -y /root/rpmbuild/SPECS/docker-c*.spec; \
  fi

COPY --from=golang /usr/local/go /usr/local/go
WORKDIR /root/rpmbuild
ENTRYPOINT ["/bin/rpmbuild"]
