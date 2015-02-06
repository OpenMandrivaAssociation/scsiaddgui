Summary:	A graphical front end for scsiadd
Name:		scsiaddgui
Version:	1.5
Release:	7
License:	GPL
URL:        	http://www.8ung.at/klappnase/scsiaddgui/scsiaddgui.html
Requires:	python, tkinter, scsiadd
Group:		System/Kernel and hardware
Source:		http://www.8ung.at/klappnase/downloads/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
BuildArch:	noarch

%description
scsiaddgui provides a GUI for the scsiadd - utility

%prep
%setup -q

%build
perl -pi -e 's!/usr/local/share!%_datadir!g' message*.py

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%_datadir/scsiaddgui
mkdir -p $RPM_BUILD_ROOT%_bindir
install --mode=755 scsiaddgui.py $RPM_BUILD_ROOT%_datadir/scsiaddgui/scsiaddgui.py
#install --mode=644 Control.py $RPM_BUILD_ROOT%_datadir/scsiaddgui/Control.py
#install --mode=644 arrow_up.xbm $RPM_BUILD_ROOT%_datadir/scsiaddgui/arrow_up.xbm
#install --mode=644 arrow_down.xbm $RPM_BUILD_ROOT%_datadir/scsiaddgui/arrow_down.xbm
#install --mode=644 messages_de.py $RPM_BUILD_ROOT%_datadir/scsiaddgui/messages_de.py
#install --mode=644 messages_en.py $RPM_BUILD_ROOT%_datadir/scsiaddgui/messages_en.py
#install --mode=644 messages.py $RPM_BUILD_ROOT%_datadir/scsiaddgui/messages.py
#install --mode=644 optionDB $RPM_BUILD_ROOT%_datadir/scsiaddgui/optionDB
install --mode=644 help_de $RPM_BUILD_ROOT%_datadir/scsiaddgui/help_de
install --mode=644 help_en $RPM_BUILD_ROOT%_datadir/scsiaddgui/help_en
install --mode=644 help_fr $RPM_BUILD_ROOT%_datadir/scsiaddgui/help_fr

mkdir -p $RPM_BUILD_ROOT%_datadir/locale/de/LC_MESSAGES
install -v --mode=644 locale/de.gmo $RPM_BUILD_ROOT%_datadir/locale/de/LC_MESSAGES/scsiaddgui.mo
mkdir -p $RPM_BUILD_ROOT%_datadir/locale/fr/LC_MESSAGES
install -v --mode=644 locale/fr.gmo $RPM_BUILD_ROOT%_datadir/locale/fr/LC_MESSAGES/scsiaddgui.mo

(cd $RPM_BUILD_ROOT
ln -s %_datadir/scsiaddgui/scsiaddgui.py ./%_bindir/scsiaddgui
)
%find_lang %name 

%files -f %name.lang
%defattr(-,root,root)
%doc doc/{ChangeLog,README}
%_bindir/scsiaddgui
%dir %_datadir/scsiaddgui
%_datadir/scsiaddgui/scsiaddgui.py
#%_datadir/scsiaddgui/Control.py
#%_datadir/scsiaddgui/arrow_up.xbm
#%_datadir/scsiaddgui/arrow_down.xbm
#%_datadir/scsiaddgui/messages_en.py
#%_datadir/scsiaddgui/messages_de.py
#%_datadir/scsiaddgui/messages.py
#%_datadir/scsiaddgui/optionDB
%_datadir/scsiaddgui/help_de
%_datadir/scsiaddgui/help_en
%_datadir/scsiaddgui/help_fr

%clean
rm -rf $RPM_BUILD_ROOT




%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.5-6mdv2010.0
+ Revision: 433634
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.5-5mdv2009.0
+ Revision: 260582
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.5-4mdv2009.0
+ Revision: 252220
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.5-2mdv2008.1
+ Revision: 140776
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Aug 09 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/09/06 16:49:58 (54906)
- rebuild

* Wed Aug 09 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/09/06 16:48:47 (54905)
Import scsiaddgui

* Tue Apr 11 2006 Lenny Cartier <lenny@mandriva.com> 1.5-1mdk
- 1.5

* Tue Aug 09 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.4-1mdk
- 1.4
- %%mkrel
- be sure to wipe out buildroot at the beginning of %%install

* Mon Nov 08 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.3-1mdk
- 1.3

* Thu Jul 08 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.2-1mdk
- 1.2

* Wed Jan 07 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.1-2mdk
- fix DIRM

* Sun Nov 02 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.1-1mdk
- 1st (real) mdk spec

* Fri Oct 31 2003 Michael Lange<klappnase@8ung.at>
- added Control.py as a replacement for the Tix.Control widget,
  so now Tix is not needed anymore, added optionDB(v.1.1)

* Mon Sep 15 2003 Michael Lange<klappnase@8ung.at>
- a little code cleanup, maybe this is the final version (v. 1.0)

