Summary:	A graphical front end for scsiadd
Name:		scsiaddgui
Version:	1.5
Release:	%mkrel 4
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


