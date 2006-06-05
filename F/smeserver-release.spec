Summary: SME Server release file
Name: smeserver-release
%define version 7.0rc3
%define displayversion %{version}
%define release 01
Version: %{version}
Release: %{release}
License: GPL
Group: System Environment/Base
#Patch0: %{name}-%{version}.patch.yyyymmddnn
Packager: SME Server developers <bugteam@contribs.org>
BuildArchitectures: noarch
Epoch: 24
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
Requires: centos-release
Obsoletes: e-smith-release
Provides: e-smith-release = %{version}-%{release}
Obsoletes: SMEServer
Provides: SMEServer = %{version}-%{release}
Obsoletes: perl-RPM
Obsoletes: pident
BuildRequires: perl, e-smith-devtools

%description
e-smith server and gateway release file

%changelog
* Mon Jun 6 2006 Gordon Rowell <gordonr@gormand.com.au> 7.0rc3-01
- Bump to rc2

* Fri Apr 7 2006 Gordon Rowell <gordonr@gormand.com.au> 7.0rc2-01
- Bump to rc2

* Tue Mar 14 2006 Gordon Rowell <gordonr@gormand.com.au> 7.0rc1-01
- Bump to rc1 

* Wed Feb 22 2006 Gordon Rowell <gordonr@gormand.com.au> 7.0pre4-01
- Bump to pre4 [SME: 860]

* Sun Feb 12 2006 Gordon Rowell <gordonr@gormand.com.au> 7.0pre3-01
- Bump to 7.0pre3 [SME: 733, 669, 721]

* Thu Jan 5 2006 Gordon Rowell <gordonr@gormand.com.au> 7.0pre1-01
- Bump to 7.0pre1

* Wed Dec 14 2005 Gordon Rowell <gordonr@gormand.com.au> 7.0beta9-02
- Obsolete/Provide SMEServer with version to match smeserver-release
- Obsolete/Provide e-smith-release with version to match smeserver-release
- [SME: 72]

* Sat Nov 19 2005 Gordon Rowell <gordonr@gormand.com.au> 7.0beta9-01
- Bump version to 7.0beta9

* Sat Nov 19 2005 Gordon Rowell <gordonr@gormand.com.au> 7.0beta8-01
- Bump version to 7.0beta8

* Mon Nov 14 2005 Gordon Rowell <gordonr@gormand.com.au> 7.0beta7-01
- Bump version to 7.0beta7

* Mon Nov 14 2005 Gordon Rowell <gordonr@gormand.com.au> 7.0beta6-03
- Package renamed to smeserver-release [SF: 1348712]

* Thu Oct 13 2005 Charlie Brady <charlieb@e-smith.com> 7.0beta6
- Bump version to 7.0beta6

* Thu Sep 29 2005 Gordon Rowell <gordonr@gormand.com.au> 7.0beta5-02
- Remove Obsoletes for redhat-release and redhat-logs [SF: 1306025]

* Thu Sep 15 2005 Charlie Brady <charlieb@e-smith.com> 7.0beta5
- Bump version to 7.0beta5

* Fri Sep 02 2005 Charlie Brady <charlieb@e-smith.com> 7.0beta4
- Bump version to 7.0beta4

* Mon Aug 29 2005 Charlie Brady <charlieb@e-smith.com> 7.0beta3-01
- Bump version to 7.0beta3

* Wed Aug 24 2005 Charlie Brady <charlieb@e-smith.com> 7.0beta2-01
- Bump version to 7.0beta2

* Wed Aug 17 2005 Charlie Brady <charlieb@e-smith.com> 7.0beta1-01
- Bump version to 7.0beta1
- Increase Epoch to be sure to trump any 6.1 or 6.2 versions.

* Thu Aug 04 2005 Charlie Brady <charlieb@e-smith.com> 7.0alpha27-01
- Bump version to 7.0alpha27

* Mon Jul 18 2005 Charlie Brady <charlieb@e-smith.com> 7.0alpha26-01
- Bump version to 7.0alpha26

* Fri Jul 15 2005 Charlie Brady <charlieb@e-smith.com> 7.0alpha25-01
- Bump version to 7.0alpha25

* Mon Jul 11 2005 Charlie Brady <charlieb@e-smith.com>
- [7.0alpha24-02]
- Remove /etc/issue.net symlink, since it clashes with a file
  in centos-release.

* Mon Jul 11 2005 Charlie Brady <charlieb@e-smith.com>
- [7.0alpha24-01]
- Bump version to 7.0alpha24

* Mon Jul 4 2005 Gordon Rowell <gordonr@gormand.com.au>
- [7.0alpha23-01]
- Bump version to 7.0alpha23
- Add dependency on centos-release
- Leave /etc/redhat-release to the centos-release package
- Add /etc/issue.net symlink and remove /etc/issue file.
- TODO: Add templates for /etc/issue{,.net}

* Fri Jun 24 2005 Charlie Brady <charlieb@e-smith.com>
- [7.0alpha22-01]
- Bump version to 7.0alpha22

* Thu Jun 16 2005 Charlie Brady <charlieb@e-smith.com>
- [7.0alpha21-01]
- Bump version to 7.0alpha21

* Fri Jun 10 2005 Charlie Brady <charlieb@e-smith.com>
- [7.0alpha20-01]
- Bump version to 7.0alpha20

* Thu Jun 09 2005 Charlie Brady <charlieb@e-smith.com>
- [7.0alpha19-01]
- Bump version to 7.0alpha19

* Mon Jun 06 2005 Charlie Brady <charlieb@e-smith.com>
- [7.0alpha18-01]
- Bump version to 7.0alpha18

* Tue May 31 2005 Charlie Brady <charlieb@e-smith.com>
- [7.0alpha17-01]
- Bump version to 7.0alpha17

* Thu May 26 2005 Charlie Brady <charlieb@e-smith.com>
- [7.0alpha16-01]
- Bump version to 7.0alpha16

* Thu May 19 2005 Charlie Brady <charlieb@e-smith.com>
- [7.0alpha15-01]
- Bump version to 7.0alpha15

* Wed May 18 2005 Charlie Brady <charlieb@e-smith.com>
- [7.0alpha14-01]
- Bump version to 7.0alpha14

* Tue May 10 2005 Charlie Brady <charlieb@e-smith.com>
- [7.0alpha12-01]
- Bump version to 7.0alpha12

* Wed May 04 2005 Charlie Brady <charlieb@e-smith.com>
- [7.0alpha10-01]
- Bump version to 7.0alpha10

* Sun May 01 2005 Charlie Brady <charlieb@e-smith.com>
- [7.0alpha9-01]
- Bump version to 7.0alpha9

* Wed Apr 27 2005 Charlie Brady <charlieb@e-smith.com>
- [7.0alpha8-01]
- Bump version to 7.0alpha8

* Tue Apr 19 2005 Charlie Brady <charlieb@e-smith.com>
- [7.0alpha7-01]
- Bump version to 7.0alpha7

* Wed Apr 13 2005 Charlie Brady <charlieb@e-smith.com>
- [7.0alpha6-01]
- Bump version to 7.0alpha6

* Fri Apr 1 2005 Charlie Brady <charlieb@e-smith.com>
- [7.0alpha5-01]
- Bump version to 7.0alpha5

* Thu Mar 17 2005 Charlie Brady <charlieb@e-smith.com>
- [7.0alpha4-01]
- Bump version to 7.0alpha4

* Wed Feb 23 2005 Charlie Brady <charlieb@e-smith.com>
- [7.0alpha3-01]
- Bump version to 7.0alpha3

* Tue Jan 04 2005 Charlie Brady <charlieb@e-smith.com>
- [7.0alpha2-01]
- Bump version to 7.0alpha2

* Tue Oct 19 2004 Charlie Brady <charlieb@e-smith.com>
- [7.0alpha1-02]
- Include /etc/redhat-release symlink [charlieb MN00052763]

* Wed Oct 13 2004 Michael Soulier <msoulier@e-smith.com>
- [7.0alpha1-01]
- Rolling to 7.0 dev - 7.0alpha1

* Sun Aug 29 2004 Michael Soulier <msoulier@e-smith.com>
- [6.2-01]
- Rolling to 6.2alpha2 - 6.2

* Tue Jul 13 2004 Michael Soulier <msoulier@e-smith.com>
- [6.1-01]
- Rolling to 6.1alpha2. [msoulier MN00040659]

* Wed Jul 16 2003 Gordon Rowell <gordon_rowell@mitel.com>
- [6.0-11]
- Bump to 6.0rc6

* Tue Jul 15 2003 Charlie Brady <charlieb@e-smith.com>
- [6.0-10]
- Bump to 6.0rc5

* Wed Jul 09 2003 Gordon Rowell <gordonr@e-smith.com>
- [6.0-09]
- Bump to 6.0rc4

* Thu Jul 03 2003 Charlie Brady <charlieb@e-smith.com>
- [6.0-08]
- Bump to 6.0rc3

* Fri Jun 27 2003 Gordon Rowell <gordonr@e-smith.com>
- [6.0-07]
- Bump to 6.0rc2

* Wed Jun 25 2003 Gordon Rowell <gordonr@e-smith.com>
- [6.0-06]
- Bump to 6.0rc1, Epoch 20->21

* Fri Jun 20 2003 Gordon Rowell <gordonr@e-smith.com>
- [6.0-05]
- Bump to 6.0beta3

* Fri Jun 20 2003 Gordon Rowell <gordonr@e-smith.com>
- [6.0-04]
- Bump to 6.0beta2

* Wed Jun  4 2003 Charlie Brady <charlieb@e-smith.com>
- [6.0-03]
- Bump to 6.0beta1.

* Fri May 30 2003 Tony Clayton <apc@e-smith.com>
- [6.0-02]
- Bump Epoch from 10 to 20 [tonyc 8870]

* Fri May  9 2003 Gordon Rowell <gordon_rowell@mitel.com>
- [6.0-01]
- Changed RPM name from e-smith-release-6.0alpha8-01 -> e-smith-release-6.0
  (alpha8 internally)
  [gordonr 8692]

* Thu Apr 24 2003 Gordon Rowell <gordonr@e-smith.com>
- [6.0alpha8-01]
- new alpha to 6.0alpha8

* Thu Apr 17 2003 Gordon Rowell <gordonr@e-smith.com>
- [6.0alpha7-01]
- new alpha to 6.0alpha7

* Wed Apr  9 2003 Gordon Rowell <gordonr@e-smith.com>
- [6.0alpha6-01]
- new alpha to 6.0alpha6

* Wed Mar 12 2003 Charlie Brady <charlieb@e-smith.com>
- [6.0alpha5-01]
- New alpha to 6.0alpha5

* Thu Mar 11 2003 Gordon Rowell <gordonr@e-smith.com>
- [6.0alpha4-02]
- Use the "version" not the "release" in the ReleaseVersion "force" 
  config template fragment. [gordonr 7531]

* Thu Mar 11 2003 Gordon Rowell <gordonr@e-smith.com>
- [6.0alpha4-01]
- Include ReleaseVersion "force" config template fragment.
  [charlieb 7531]

* Thu Feb 27 2003 Gordon Rowell <gordonr@e-smith.com>
- [6.0alpha3-01]
- New alpha to 6.0alpha3

* Tue Dec 03 2002 Charlie Brady <charlieb@e-smith.com> 6.0alpha2-01
- New alpha release.

* Fri Nov 15 2002 Charlie Brady <charlieb@e-smith.com> 6.0alpha1-01
- New alpha release. Note that the first alpha of what became 5.6
  was called 6.0alpha1, and there were subsequent alphas in that
  range. Those releases were and are completely unsupported, and
  we do not support upgrades of those servers. We'll ignore the
  version clash between those prototypes and this development
  version.

* Thu Oct 17 2002 Charlie Brady <charlieb@e-smith.com> 5.6beta11-01
- New beta release.

* Tue Oct 15 2002 Gordon Rowell <gordonr@e-smith.com> 5.6beta10-01
- New beta release.

* Tue Oct 15 2002 Gordon Rowell <gordonr@e-smith.com> 5.6beta9-01
- New beta release - back to 5.6beta9 - drop Epoch back to 9 as for
  previous betas.

* Mon Oct 14 2002 Charlie Brady <charlieb@e-smith.com> 5.6-01
- Roll version for 5.6 release candidate.
- Bump Serial and rename to preferred Epoch tag name.

* Thu Oct 10 2002 Charlie Brady <charlieb@e-smith.com> 5.6beta8-01
- New beta release.

* Thu Oct 10 2002 Charlie Brady <charlieb@e-smith.com> 5.6beta7-01
- New beta release.

* Wed Oct 09 2002 Gordon Rowell <gordonr@e-smith.com> 5.6beta6-01
- New beta release.

* Fri Oct 04 2002 Charlie Brady <charlieb@e-smith.com> 5.6beta5-01
- New beta release.

* Wed Oct 02 2002 Charlie Brady <charlieb@e-smith.com> 5.6beta4-01
- New beta release.

* Mon Sep 23 2002 Charlie Brady <charlieb@e-smith.com> 5.6beta3-02
- Add Obsoletes header to remove orphaned pidentd [charlieb 4743].

* Mon Sep 23 2002 Charlie Brady <charlieb@e-smith.com> 5.6beta3-01
- New beta release

* Thu Sep 19 2002 Charlie Brady <charlieb@e-smith.com> 5.6beta2-01
- New beta release.

* Thu Sep 05 2002 Charlie Brady <charlieb@e-smith.com> 5.6beta1-01
- New beta release.

* Fri Aug 30 2002 Charlie Brady <charlieb@e-smith.com> 5.6alpha8-01
- New alpha release.

* Fri Aug 30 2002 Charlie Brady <charlieb@e-smith.com> 5.6alpha7-01
- New alpha release.

* Tue Aug 06 2002 Charlie Brady <charlieb@e-smith.com> 5.6alpha6-01
- Next release will be called 5.6. Change version number, and bump
  Serial header.

* Wed Jul 31 2002 Charlie Brady <charlieb@e-smith.com>
- [6.0alpha6-01]
- Bump to alpha6 release.

* Thu Jul 18 2002 Charlie Brady <charlieb@e-smith.com>
- [6.0alpha5-01]
- Bump to alpha5 release.

* Tue Jul 02 2002 Charlie Brady <charlieb@e-smith.com>
- [6.0alpha4-01]
- Bump to alpha4 release.

* Wed Jun 19 2002 Charlie Brady <charlieb@e-smith.com>
- [6.0alpha3-01]
- Add 2.4 kernel, upgrade some packages to suit, and remove
  some packages which are 2.2.x kernel reliant.

* Mon Jun 03 2002 Charlie Brady <charlieb@e-smith.com>
- [5.5-02]
- Bump revision for second release candidate.

* Sun Jun 02 2002 Charlie Brady <charlieb@e-smith.com>
- [5.5-01]
- Bump version for 5.5 release candidate.

* Fri May 31 2002 Charlie Brady <charlieb@e-smith.com>
- [5.5beta10-01]
- Bump version for 5.5beta10 release.

* Wed May 29 2002 Charlie Brady <charlieb@e-smith.com>
- [5.5beta9-01]
- Bump version for 5.5beta9 release.

* Tue May 28 2002 Gordon Rowell <gordonr@e-smith.com>
- [5.5beta8-01]
- Bump version for 5.5beta8 release.

* Thu May 23 2002 Charlie Brady <charlieb@e-smith.com>
- [5.5beta7-01]
- Bump version for 5.5beta7 release.

* Thu May 23 2002 Charlie Brady <charlieb@e-smith.com>
- [5.5beta6-01]
- Bump version for 5.5beta6 release.
- remove foot.tmpl and noframes_foot.tmpl - re-adding in e-smith-base 
  [tonyc 3223] 

* Fri May 17 2002 Gordon Rowell <gordonr@e-smith.com>
- [5.5beta5-01]
- Bump version for 5.5beta5 release.

* Fri May 17 2002 Gordon Rowell <gordonr@e-smith.com>
- [5.5beta4-01]
- Bump version for 5.5beta4 release.

* Tue May 14 2002 Charlie Brady <charlieb@e-smith.com>
- [5.5beta3-01]
- Bump version for 5.5beta3 release.

* Tue May 14 2002 Charlie Brady <charlieb@e-smith.com>
- [5.5beta2-01]
- Bump version for 5.5beta2 release.

* Thu May 09 2002 Gordon Rowell <gordonr@e-smith.com>
- [5.5beta1-01]

* Wed May 08 2002 Gordon Rowell <gordonr@e-smith.com>
- [5.5alpha5-05]
- Generate noframes_foot.tmpl as well [gordonr 3223]

* Wed May 08 2002 Gordon Rowell <gordonr@e-smith.com>
- [5.5alpha5-04]
- Actually copy the foot.tmpl file in %build [gordonr 3223]

* Wed May 08 2002 Gordon Rowell <gordonr@e-smith.com>
- [5.5alpha5-03]
- Generate /etc/e-smith/web/common/foot.tmpl as a workaround 
  for Text::Template untainting problem in CGI::FormMagick [gordonr 3223, 3771]
- Manually patched 5.5alpha5-03 [gordonr 3223]

* Wed May 08 2002 Tony Clayton <tonyc@e-smith.com>
- [5.5alpha5-03]
- Generate /etc/e-smith/web/common/foot.tmpl as a workaround 
- added Obsoletes: perl-RPM for 5.1.X -> 5.5 migration [tonyc 3355]
- added patch to 5.5alpha5-02 also  [tonyc 3355]

* Mon May 06 2002 Gordon Rowell <gordonr@e-smith.com>
- [5.5alpha5-01]

* Tue Apr 30 2002 Gordon Rowell <gordonr@e-smith.com>
- [5.5alpha4-01]

* Tue Apr 30 2002 Gordon Rowell <gordonr@e-smith.com>
- [5.5alpha3-02]
- CVS import

* Tue Apr 30 2002 Gordon Rowell <gordonr@e-smith.com>
- [5.5alpha3-01]

* Thu Apr 04 2002 Gordon Rowell <gordonr@e-smith.com>
- [5.5alpha2-01]

* Thu Feb 14 2002 Charlie Brady <charlieb@e-smith.com>
- [5.5alpha1-01]
- Initial, for the first alpha.

%prep

%build

%install
mkdir -p $RPM_BUILD_ROOT/etc
echo "SME Server release %{displayversion}" >\
 $RPM_BUILD_ROOT/etc/e-smith-release
mkdir -p $RPM_BUILD_ROOT/etc/e-smith/db/configuration/force/sysconfig
echo "%{displayversion}" \
   > $RPM_BUILD_ROOT/etc/e-smith/db/configuration/force/sysconfig/ReleaseVersion
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
    > %{name}-%{version}-%{release}-filelist

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
