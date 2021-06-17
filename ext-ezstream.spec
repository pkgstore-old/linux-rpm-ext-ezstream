%global app                     ezstream
%global d_bin                   %{_bindir}
%global release_prefix          100

Name:                           ext-ezstream
Version:                        1.0.1
Release:                        %{release_prefix}%{?dist}
Summary:                        META-package for install and configure Ezstream
License:                        MIT

Source10:                       %{app}.local.xml
Source20:                       %{app}.run.sh
Source21:                       %{app}.playlist.sh

Requires:                       ezstream screen

%description
META-package for install and configure Ezstream.

# -------------------------------------------------------------------------------------------------------------------- #
# -----------------------------------------------------< SCRIPT >----------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

%prep


%install
%{__rm} -rf %{buildroot}

%{__install} -Dp -m 0644 %{SOURCE10} \
  %{buildroot}%{_sysconfdir}/%{app}.local.xml
%{__install} -Dp -m 0755 %{SOURCE20} \
  %{buildroot}%{d_bin}/%{app}.run.sh
%{__install} -Dp -m 0755 %{SOURCE21} \
  %{buildroot}%{d_bin}/%{app}.playlist.sh


%files
%config %{_sysconfdir}/%{app}.local.xml
%{d_bin}/%{app}.run.sh
%{d_bin}/%{app}.playlist.sh


%changelog
* Thu Jun 17 2021 Package Store <kitsune.solar@gmail.com> - 1.0.1-100
- UPD: Move to GitHub.
- UPD: License.
- UPD: "ezstream.playlist.sh".
- UPD: "ezstream.run.sh".

* Thu Aug 01 2019 Package Store <pkgstore@pm.me> - 1.0.0-107
- UPD: Shell scripts.

* Wed Jul 31 2019 Package Store <pkgstore@pm.me> - 1.0.0-106
- UPD: SPEC-file.

* Tue Jul 02 2019 Package Store <pkgstore@pm.me> - 1.0.0-105
- UPD: build script.
- UPD: SPEC-file.

* Sun Mar 31 2019 Package Store <pkgstore@pm.me> - 1.0.0-104
- UPD: "run.ezstream.playlist.sh".

* Sun Mar 31 2019 Package Store <pkgstore@pm.me> - 1.0.0-103
- UPD: "run.ezstream.playlist.sh".

* Sun Mar 31 2019 Package Store <pkgstore@pm.me> - 1.0.0-102
- UPD: "run.ezstream.playlist.sh".

* Sun Mar 31 2019 Package Store <pkgstore@pm.me> - 1.0.0-101
- UPD: "run.ezstream.playlist.sh".

* Sun Mar 31 2019 Package Store <pkgstore@pm.me> - 1.0.0-100
- Initial build.
