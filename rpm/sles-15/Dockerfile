ARG GO_IMAGE
ARG DISTRO=sles
ARG SUITE=15
ARG BUILD_IMAGE=dockereng/${DISTRO}:${SUITE}-s390x


FROM ${GO_IMAGE} AS golang

FROM ${BUILD_IMAGE}
ENV GOPROXY=direct
ENV GO111MODULE=off
ENV GOPATH=/go
ENV PATH $PATH:/usr/local/go/bin:$GOPATH/bin
ENV AUTO_GOPATH 1
ENV DOCKER_BUILDTAGS seccomp selinux
ENV RUNC_BUILDTAGS seccomp selinux
ARG DISTRO
ARG SUITE
ENV DISTRO=${DISTRO}
ENV SUITE=${SUITE}
ENV CC=gcc
USER root

COPY SPECS /usr/src/packages/SPECS
COPY rpmbuild/SOURCES/ /usr/src/packages/SOURCES/
RUN zypper -n install $(rpmspec --parse /usr/src/packages/SPECS/sles_dependencies.spec | grep BuildRequires | cut -d' ' -f2 | xargs)
RUN rpmbuild -bb /usr/src/packages/SPECS/policycoreutils.spec
RUN rpmbuild -bb /usr/src/packages/SPECS/checkpolicy.spec 
RUN rpm -i /usr/src/packages/RPMS/s390x/policycoreutils-3.2-1.s390x.rpm && rpm -i /usr/src/packages/RPMS/s390x/checkpolicy-3.2.61.1-1.s390x.rpm \
&& sles_version=$(lsb_release -r | rev | cut -c1) \
&& opensuse_repo="https://download.opensuse.org/repositories/security:SELinux/SLE_15_SP$sles_version/security:SELinux.repo" \
&& zypper addrepo $opensuse_repo \
&& zypper --gpg-auto-import-keys refresh && zypper install -y selinux-policy selinux-policy-devel \
&& mkdir -p /root/rpmbuild/ && cp -r /usr/src/packages/* /root/rpmbuild/

# TODO change once we support scan-plugin on other architectures
RUN \
  if [ "$(uname -m)" = "x86" ]; then \
    rpmbuild /root/rpmbuild/SPECS/*.spec; \
  else \
     rpmbuild /usr/src/packages/SPECS/docker-c*.spec; \
  fi

COPY --from=golang /usr/local/go /usr/local/go
WORKDIR /root/rpmbuild
ENTRYPOINT ["/usr/bin/rpmbuild"]
