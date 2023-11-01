Name:          gnome-disk-utility
Version:       3.28.3
Release:       2%{?dist}
Summary:       Disks

License:       GPLv2+
URL:           https://git.gnome.org/browse/gnome-disk-utility
Source0:       https://download.gnome.org/sources/%{name}/3.28/%{name}-%{version}.tar.xz

BuildRequires: /usr/bin/appstream-util
BuildRequires: desktop-file-utils
BuildRequires: docbook-style-xsl
BuildRequires: gettext
# for xsltproc
BuildRequires: libxslt
BuildRequires: meson
BuildRequires: pkgconfig(dvdread)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libcanberra-gtk3)
BuildRequires: pkgconfig(liblzma)
BuildRequires: pkgconfig(libnotify)
BuildRequires: pkgconfig(libsecret-1)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: pkgconfig(pwquality)
BuildRequires: pkgconfig(udisks2)
BuildRequires: python3-devel

Requires:      udisks2

%description
This package contains the Disks and Disk Image Mounter applications.
Disks supports partitioning, file system creation, encryption,
fstab/crypttab editing, ATA SMART and other features

%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{name}


%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.gnome.DiskUtility.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{name}.lang
%doc AUTHORS NEWS README
%license COPYING
%{_bindir}/gnome-disks
%{_bindir}/gnome-disk-image-mounter
%{_datadir}/applications/org.gnome.DiskUtility.desktop
%{_datadir}/applications/gnome-disk-image-mounter.desktop
%{_datadir}/applications/gnome-disk-image-writer.desktop
%{_datadir}/dbus-1/services/org.gnome.DiskUtility.service
%{_datadir}/glib-2.0/schemas/org.gnome.Disks.gschema.xml
%{_datadir}/icons/hicolor/*/apps/gnome-disks*
%{_datadir}/metainfo/org.gnome.DiskUtility.appdata.xml
%{_mandir}/man1/*
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.DiskUtilityNotify.desktop
%{_libexecdir}/gsd-disk-utility-notify


%changelog
* Mon Aug 13 2018 Troy Dawson <tdawson@redhat.com> - 3.28.3-2
- Add BuildRequest python3-devel

* Fri Jun 01 2018 Kalev Lember <klember@redhat.com> - 3.28.3-1
- Update to 3.28.3

* Tue May 08 2018 Kalev Lember <klember@redhat.com> - 3.28.2-1
- Update to 3.28.2

* Mon Apr 09 2018 Kalev Lember <klember@redhat.com> - 3.28.1-1
- Update to 3.28.1

* Mon Mar 12 2018 Kalev Lember <klember@redhat.com> - 3.28.0-1
- Update to 3.28.0

* Mon Mar 05 2018 Kalev Lember <klember@redhat.com> - 3.27.92-1
- Update to 3.27.92

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.27.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.27.1-2
- Remove obsolete scriptlets

* Thu Nov 02 2017 Kalev Lember <klember@redhat.com> - 3.27.1-1
- Update to 3.27.1

* Wed Nov 01 2017 Kalev Lember <klember@redhat.com> - 3.26.2-1
- Update to 3.26.2

* Sun Oct 08 2017 Kalev Lember <klember@redhat.com> - 3.26.1-1
- Update to 3.26.1

* Mon Sep 11 2017 Kalev Lember <klember@redhat.com> - 3.26.0-1
- Update to 3.26.0

* Tue Sep 05 2017 Kalev Lember <klember@redhat.com> - 3.25.92-1
- Update to 3.25.92

* Mon Aug 28 2017 Kalev Lember <klember@redhat.com> - 3.25.91-1
- Update to 3.25.91

* Tue Aug 15 2017 Kalev Lember <klember@redhat.com> - 3.25.90-1
- Update to 3.25.90

* Mon Jul 31 2017 Kalev Lember <klember@redhat.com> - 3.25.4-1
- Update to 3.25.4
- Switch to the meson build system

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.25.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 12 2017 Kalev Lember <klember@redhat.com> - 3.25.2-1
- Update to 3.25.2

* Tue May 09 2017 Kalev Lember <klember@redhat.com> - 3.24.1-1
- Update to 3.24.1

* Tue Mar 21 2017 Kalev Lember <klember@redhat.com> - 3.24.0-1
- Update to 3.24.0

* Sat Mar 11 2017 Richard Hughes <rhughes@redhat.com> - 3.23.92-1
- Update to 3.23.92

* Mon Feb 13 2017 Richard Hughes <rhughes@redhat.com> - 3.23.4-1
- Update to 3.23.4

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Nov 24 2016 Kalev Lember <klember@redhat.com> - 3.22.1-1
- Update to 3.22.1

* Mon Sep 19 2016 Kalev Lember <klember@redhat.com> - 3.22.0-1
- Update to 3.22.0

* Sat Sep 03 2016 Kalev Lember <klember@redhat.com> - 3.21.91-1
- Update to 3.21.91
- Don't set group tags

* Wed Jun 22 2016 Richard Hughes <rhughes@redhat.com> - 3.21.3-1
- Update to 3.21.3

* Sun May 08 2016 Kalev Lember <klember@redhat.com> - 3.20.2-1
- Update to 3.20.2

* Wed Apr 13 2016 Kalev Lember <klember@redhat.com> - 3.20.1-1
- Update to 3.20.1

* Tue Mar 22 2016 Kalev Lember <klember@redhat.com> - 3.20.0-1
- Update to 3.20.0

* Thu Feb 04 2016 David King <amigadave@amigadave.com> - 3.19.3-3
- Use global rather than define

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 11 2015 Kalev Lember <klember@redhat.com> - 3.19.3-1
- Update to 3.19.3

* Fri Nov 27 2015 Michael Catanzaro <mcatanzaro@gnome.org> - 3.18.3.1-1
- Update to 3.18.3.1

* Tue Nov 10 2015 Kalev Lember <klember@redhat.com> - 3.18.2-1
- Update to 3.18.2

* Mon Oct 12 2015 Kalev Lember <klember@redhat.com> - 3.18.1-1
- Update to 3.18.1

* Thu Oct 01 2015 Michael Catanzaro <mcatanzaro@gnome.org> - 3.18.0-3
- Bump NVR

* Tue Sep 29 2015 Michael Catanzaro <mcatanzaro@gnome.org> - 3.18.0-2
- Add X-GNOME-Utilities desktop category

* Mon Sep 21 2015 Kalev Lember <klember@redhat.com> - 3.18.0-1
- Update to 3.18.0

* Sat Aug 29 2015 Kalev Lember <klember@redhat.com> - 3.17.91-1
- Update to 3.17.91
- Use make_install macro

* Sun Jun 21 2015 David King <amigadave@amigadave.com> - 3.17.3-1
- Update to 3.17.3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.17.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 David King <amigadave@amigadave.com> - 3.17.2-2
- Fix font rendering in benchmark dialog (#598277)

* Mon May 25 2015 David King <amigadave@amigadave.com> - 3.17.2-1
- Update to 3.17.2
- Validate AppData in check

* Tue May 12 2015 David King <amigadave@amigadave.com> - 3.16.1-1
- Update to 3.16.1
- Use license macro for COPYING

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 3.16.0-2
- Add an AppData file for the software center

* Mon Mar 23 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.0-1
- Update to 3.16.0

* Wed Nov 12 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.0-1
- Update to 3.14.0

* Tue Oct 07 2014 David King <amigadave@amigadave.com> - 3.12.1-7
- Remove obsolete Obsoletes (#1002112)

* Thu Sep 11 2014 David King <amigadave@amigadave.com> - 3.12.1-6
- Fix header bar button positions
- Preserve timestamps during installation

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 07 2014 Kalev Lember <kalevlember@gmail.com> - 3.12.1-3
- Drop gnome-icon-theme-symbolic dependency

* Fri May 02 2014 David King <amigadave@amigadave.com> - 3.12.1-2
- Fix desktop database scriptlet (#685030)
- Use pkgconfig for BuildRequires
- Fix bogus dates in changelog

* Mon Apr 28 2014 Richard Hughes <rhughes@redhat.com> - 3.12.1-1
- Update to 3.12.1

* Sun Mar 23 2014 Kalev Lember <kalevlember@gmail.com> - 3.12.0-1
- Update to 3.12.0

* Mon Feb 17 2014 Richard Hughes <rhughes@redhat.com> - 3.11.0-1
- Update to 3.11.0

* Sun Sep 29 2013 Kalev Lember <kalevlember@gmail.com> - 3.10.0-1
- Update to 3.10.0

* Thu Aug 22 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.0-1
- Update to 3.9.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 02 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.2-1
- Update to 3.8.2

* Wed Mar 20 2013 Richard Hughes <rhughes@redhat.com> - 3.8.0-1
- Update to 3.8.0

* Mon Feb 25 2013 Kalev Lember <kalevlember@gmail.com> - 3.7.2-2
- Require gnome-icon-theme-symbolic (#910982)

* Tue Feb 19 2013 Richard Hughes <rhughes@redhat.com> - 3.7.2-1
- Update to 3.7.2

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 07 2013 David Zeuthen <davidz@redhat.com> - 3.7.1-1%{?dist}
- Update to 3.7.1

* Fri Dec 21 2012 David Zeuthen <davidz@redhat.com> - 3.7.0-4%{?dist}
- Add files for the new gnome-settings-daemon plug-in

* Fri Dec 21 2012 David Zeuthen <davidz@redhat.com> - 3.7.0-3%{?dist}
- BR gnome-settings-daemon 3.7.3 and rebuild without --disable-gsd-plugin

* Tue Dec 18 2012 David Zeuthen <davidz@redhat.com> - 3.7.0-2%{?dist}
- Adjust BRs

* Tue Dec 18 2012 David Zeuthen <davidz@redhat.com> - 3.7.0-1%{?dist}
- Update to 3.7.0

* Fri Oct 05 2012 David Zeuthen <davidz@redhat.com> - 3.6.1-1%{?dist}
- Update to 3.6.1

* Sat Sep 22 2012 Kalev Lember <kalevlember@gmail.com> - 3.6.0-1
- Update to 3.6.0
- Drop the -Werror patch; applied upstream
- Add glib-compile-schemas scriptlets
- Relicensed from LGPLv2+ to GPLv2+

* Fri Jul 27 2012 David Zeuthen <davidz@redhat.com> - 3.5.3-2%{?dist}
- Avoid treating warnings as errors

* Fri Jul 27 2012 David Zeuthen <davidz@redhat.com> - 3.5.3-1%{?dist}
- Update to 3.5.3

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 10 2012 Ville Skyttä <ville.skytta@iki.fi> - 3.5.2-2
- Own the %%{_datadir}/gnome-disk-utility dir.

* Tue Jun 05 2012 David Zeuthen <davidz@redhat.com> - 3.5.2-1%{?dist}
- Update to 3.5.2

* Wed May 09 2012 David Zeuthen <davidz@redhat.com> - 3.5.1-4%{?dist}
- BR docbook-style-xsl for man pages

* Wed May 09 2012 David Zeuthen <davidz@redhat.com> - 3.5.1-3%{?dist}
- BR libxslt (for xsltproc)

* Wed May 09 2012 David Zeuthen <davidz@redhat.com> - 3.5.1-2%{?dist}
- BR libgnome-keyring-devel and systemd-devel

* Wed May 09 2012 David Zeuthen <davidz@redhat.com> - 3.5.1-1%{?dist}
- Update to 3.5.1

* Mon Apr 30 2012 Richard Hughes <hughsient@gmail.com> - 3.4.1-1
- Update to 3.4.1

* Mon Mar 26 2012 David Zeuthen <davidz@redhat.com> - 3.4.0-1%{?dist}
- Update to release 3.4.0

* Mon Mar 05 2012 David Zeuthen <davidz@redhat.com> - 3.3.93-1%{?dist}
- Update to release 3.3.93

* Thu Feb 23 2012 David Zeuthen <davidz@redhat.com> - 3.3.92-1%{?dist}
- Update to release 3.3.92

* Mon Feb 06 2012 David Zeuthen <davidz@redhat.com> - 3.3.91-1%{?dist}
- Update to release 3.3.91

* Tue Jan 24 2012 David Zeuthen <davidz@redhat.com> - 3.3.90-3%{?dist}
- Require udisks2 package (for the daemon) (#783974)

* Fri Jan 20 2012 David Zeuthen <davidz@redhat.com> - 3.3.90-2%{?dist}
- Rebuild

* Fri Jan 20 2012 David Zeuthen <davidz@redhat.com> - 3.3.90-1%{?dist}
- Update to release 3.3.90

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 08 2011 Adam Jackson <ajax@redhat.com> - 3.0.2-4
- Rebuild to break bogus libpng dep

* Mon Jul 11 2011 David Zeuthen <davidz@redhat.com> - 3.0.2-3%{?dist}
- BR gtk-doc

* Mon Jul 11 2011 David Zeuthen <davidz@redhat.com> - 3.0.2-2%{?dist}
- BR gnome-common

* Mon Jul 11 2011 David Zeuthen <davidz@redhat.com> - 3.0.2-1%{?dist}
- Update to 3.0.2

* Sat May 07 2011 Christopher Aillon <caillon@redhat.com> - 3.0.0-2
- Update icon cache scriptlet

* Mon Apr  4 2011 Matthias Clasen <mclasen@redhat.com> - 3.0.0-1
- Update to 3.0.0

* Mon Mar 21 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.7-1
- Update to 2.91.7

* Mon Mar 14 2011 Tomas Bzatek <tbzatek@redhat.com> - 2.91.6-5
- Fix gnome-disk-utility-nautilus upgrade path

* Tue Feb 22 2011 Tomas Bzatek <tbzatek@redhat.com> - 2.91.6-4
- Split nautilus extension into a separate package

* Fri Feb 11 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.6-3
- Rebuild against newer gtk

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.91.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb  2 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.6-1%{?dist}
- Update to 2.91.6

* Wed Feb  2 2011 Matthias Clasen <mclasen@redhat.com> - 2.32.1-4%{?dist}
- Rebuild against newer gtk

* Fri Jan  7 2011 Matthias Clasen <mclasen@redhat.com> - 2.32.1-3%{?dist}
- Rebuild against new gtk

* Fri Dec  3 2010 Matthias Clasen <mclasen@redhat.com> - 2.32.1-2%{?dist}
- Rebuild against new gtk

* Thu Nov 11 2010 Matthias Clasen <mclasen@redhat.com> - 2.32.1-1%{?dist}
- 2.32.1

* Fri Nov  5 2010 Matthias Clasen <mclasen@redhat.com> - 2.32.0-3%{?dist}
- Fix a problem with 'disk failure' notifications

* Wed Nov  3 2010 Matthias Clasen <mclasen@redhat.com> - 2.32.0-2%{?dist}
- Rebuild against libnotify 0.7.0

* Tue Sep 28 2010 Matthias Clasen <mclasen@redhat.com> - 2.32.0-1%{?dist}
- Update to 2.32.0

* Wed Jun 16 2010 Matthias Clasen <mclasen@redhat.com> - 2.30.1-2%{?dist}
- Kill the scrollkeeper runtime dep

* Mon Mar 22 2010 David Zeuthen <davidz@redhat.com> - 2.30.1-1%{?dist}
- Update to 2.30.1

* Mon Mar 15 2010 David Zeuthen <davidz@redhat.com> - 2.30.0-1%{?dist}
- Update to 2.30.0

* Tue Feb 23 2010 David Zeuthen <davidz@redhat.com> - 2.29.90-1%{?dist}
- Update to 2.29.90

* Mon Feb 15 2010 David Zeuthen <davidz@redhat.com> - 2.29.0-0.git20100215.3%{?dist}
- Add rarian-compat to BR

* Mon Feb 15 2010 David Zeuthen <davidz@redhat.com> - 2.29.0-0.git20100215.1%{?dist}
- Update to git snapshot
- Drop upstreamed patches

* Mon Jan 18 2010 Tomas Bzatek <tbzatek@redhat.com> - 2.29.0-0.git20100115.2%{?dist}
- Install missing include

* Fri Jan 15 2010 David Zeuthen <davidz@redhat.com> - 2.29.0-0.git20100115.1%{?dist}
- BR avahi-ui-devel

* Fri Jan 15 2010 David Zeuthen <davidz@redhat.com> - 2.29.0-0.git20100115%{?dist}
- Update to git snapshot

* Wed Dec  2 2009 David Zeuthen <davidz@redhat.com> - 2.29.0-0.git20091202%{?dist}
- Update to git snapshot that requires udisks instead of DeviceKit-disks
- The UI has been completely revamped

* Fri Sep 18 2009 David Zeuthen <davidz@redhat.com> - 2.28.0-2%{?dist}
- BR libatasmart-devel

* Fri Sep 18 2009 David Zeuthen <davidz@redhat.com> - 2.28.0-1%{?dist}
- Update to upstream release 2.28.0
- Compared to previous releases, this release should whine less about SMART

* Mon Aug 17 2009 David Zeuthen <davidz@redhat.com> - 0.5-3%{?dist}
- Drop upstreamed patch

* Mon Aug 17 2009 David Zeuthen <davidz@redhat.com> - 0.5-2%{?dist}
- Rebuild

* Mon Aug 17 2009 David Zeuthen <davidz@redhat.com> - 0.5-1%{?dist}
- Update to release 0.5

* Mon Jul 27 2009 Matthias Clasen <mclasen@redhat.com> - 0.4-3%{?dist}
- Drop PolicyKit from .pc files, too

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 19 2009 David Zeuthen <davidz@redhat.com> - 0.4-1%{?dist}
- Update to release 0.4

* Fri May 01 2009 David Zeuthen <davidz@redhat.com> - 0.3-1%{?dist}
- Upstream release 0.3

* Wed Apr 15 2009 David Zeuthen <davidz@redhat.com> - 0.3-0.5.20090415git%{?dist}
- New snapshot

* Sun Apr 12 2009 David Zeuthen <davidz@redhat.com> - 0.3-0.4.20090412git%{?dist}
- New snapshot

* Fri Apr 10 2009 Matthias Clasen <mclasen@redhat.com> - 0.3-0.3.20090406git%{?dist}
- Don't own directories that belong to hicolor-icon-theme

* Wed Apr 08 2009 David Zeuthen <davidz@redhat.com> - 0.3-0.2.20090406git%{?dist}
- Fix bug in detecting when a PolicyKit error is returned (#494787)

* Mon Apr 06 2009 David Zeuthen <davidz@redhat.com> - 0.3-0.1.20090406git%{?dist}
- New snapshot

* Wed Mar 04 2009 David Zeuthen <davidz@redhat.com> - 0.2-2%{?dist}
- Don't crash when changing the LUKS passphrase on a device

* Mon Mar 02 2009 David Zeuthen <davidz@redhat.com> - 0.2-1%{?dist}
- Update to version 0.2

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.git20080720.2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 27 2009 Matthias Clasen <mclasen@redhat.com> 0.1-0.git20080720.2%{?dist}
- Rebuild for pkgconfig provides

* Sun Nov 23 2008 Matthias Clasen <mclasen@redhat.com> 0.1-0.git20080720.1%{?dist}
- Improve %%summary and %%description

* Sun Jul 20 2008 David Zeuthen <davidz@redhat.com> - 0.1-0.git20080720%{?dist}
- Initial Packaging
