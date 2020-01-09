Name:           codehaus-parent
Version:        4
Release:        5%{?dist}
Summary:        Parent pom file for codehaus projects

Group:          Development/Libraries
License:        ASL 2.0
URL:            http://codehaus.org/
#Next version with license is at https://github.com/sonatype/codehaus-parent/blob/master/pom.xml
Source0:        http://repo1.maven.org/maven2/org/codehaus/codehaus-parent/%{version}/codehaus-parent-%{version}.pom
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
Patch0:         %{name}-enforcer.patch
BuildArch:      noarch

BuildRequires:  jpackage-utils

Requires:       jpackage-utils

%description
This package contains the parent pom file for codehaus projects.


%prep
%setup -q -c -T
cp -p %{SOURCE0} .
cp -p %{SOURCE1} LICENSE
%patch0

%build


%install
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 codehaus-parent-%{version}.pom \
        $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom 


%files
%doc LICENSE
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 4-5
- Mass rebuild 2013-12-27

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Aug 16 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 4-3
- Install LICENSE

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 3 2012 Orion Poplawski <orion@cora.nwra.com> - 4-1
- Update to version 4

* Tue May 22 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3-5
- Patch enforcer plugin out so it's not needed in all child packages

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu May 5 2011 Orion Poplawski <orion@cora.nwra.com> - 3-3
- Strip requires

* Wed May 4 2011 Orion Poplawski <orion@cora.nwra.com> - 3-2
- Drop build and defattr
- Better summary/description
- Upstream set license to ASL 2.0

* Fri Apr 29 2011 Orion Poplawski <orion@cora.nwra.com> - 3-1
- Initial package
