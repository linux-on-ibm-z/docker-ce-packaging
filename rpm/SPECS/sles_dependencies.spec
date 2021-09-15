Name:       SLES_Dependencies
Version:    %{_version}
License:    GPLv2
Release:    1%{?dist}
Summary:    SLES Dependencies

%description
The file lists the dependencies required for building the rpmbuild-sles-15

BuildRequires: rpm-build
BuildRequires: rpmlint
BuildRequires: pkg-config
BuildRequires: libsystemd0
BuildRequires: systemd-devel
BuildRequires: selinux-tools
BuildRequires: wget
BuildRequires: cmake
BuildRequires: device-mapper-devel
BuildRequires: git
BuildRequires: glibc-devel-static
BuildRequires: libseccomp-devel
BuildRequires: libtool
BuildRequires: libarchive-devel
BuildRequires: btrfsprogs
BuildRequires: libbtrfs-devel
BuildRequires: lsb-release
BuildRequires: gzip
BuildRequires: make
BuildRequires: gcc7
BuildRequires: flex
BuildRequires: libbz2-devel
BuildRequires: libsemanage-devel
BuildRequires: libsepol-devel
BuildRequires: gettext
BuildRequires: bison
BuildRequires: tar
