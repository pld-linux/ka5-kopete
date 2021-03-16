%define		kdeappsver	20.12.3
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		kopete
Summary:	kopete
Name:		ka5-%{kaname}
Version:	20.12.3
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	7bbe07decde1154cc7924ca566a97c4c
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Sql-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	Qt5Xml-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	gpgme-c++-devel >= 1.8.0
BuildRequires:	ka5-kidentitymanagement-devel >= %{kdeappsver}
BuildRequires:	ka5-libkleo-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kcmutils-devel >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kcontacts-devel >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf5-kdelibs4support-devel >= %{kframever}
BuildRequires:	kf5-kdnssd-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-kemoticons-devel >= %{kframever}
BuildRequires:	kf5-khtml-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kio-devel >= %{kframever}
BuildRequires:	kf5-knotifyconfig-devel >= %{kframever}
BuildRequires:	kf5-kparts-devel >= %{kframever}
BuildRequires:	kf5-ktexteditor-devel >= %{kframever}
BuildRequires:	kf5-kwallet-devel >= %{kframever}
BuildRequires:	mediastreamer-devel
BuildRequires:	ninja
BuildRequires:	ortp-devel
BuildRequires:	phonon-qt5-devel
BuildRequires:	qca-qt5-devel >= 2.1.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kopete is an instant messenger supporting AIM, ICQ, Windows Live
Messenger, Yahoo, Jabber, Gadu-Gadu, Novell GroupWise Messenger, and
more. It is designed to be a flexible and extensible multi-protocol
system suitable for personal and enterprise use.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/sr
%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/kopeterc
%attr(755,root,root) %{_bindir}/kopete
%attr(755,root,root) %{_bindir}/winpopup-install
%attr(755,root,root) %{_bindir}/winpopup-send
%attr(755,root,root) %ghost %{_libdir}/libkopete.so.1
%attr(755,root,root) %{_libdir}/libkopete.so.1.*.*
%attr(755,root,root) %ghost %{_libdir}/libkopete_oscar.so.1
%attr(755,root,root) %{_libdir}/libkopete_oscar.so.1.*.*
%attr(755,root,root) %ghost %{_libdir}/libkopete_videodevice.so.1
%attr(755,root,root) %{_libdir}/libkopete_videodevice.so.1.*.*
%attr(755,root,root) %ghost %{_libdir}/libkopeteaddaccountwizard.so.1
%attr(755,root,root) %{_libdir}/libkopeteaddaccountwizard.so.1.*.*
%attr(755,root,root) %ghost %{_libdir}/libkopetechatwindow_shared.so.1
%attr(755,root,root) %{_libdir}/libkopetechatwindow_shared.so.1.*.*
%attr(755,root,root) %ghost %{_libdir}/libkopetecontactlist.so.1
%attr(755,root,root) %{_libdir}/libkopetecontactlist.so.1.*.*
%attr(755,root,root) %ghost %{_libdir}/libkopeteidentity.so.1
%attr(755,root,root) %{_libdir}/libkopeteidentity.so.1.*.*
%attr(755,root,root) %ghost %{_libdir}/libkopeteprivacy.so.1
%attr(755,root,root) %{_libdir}/libkopeteprivacy.so.1.*.*
%attr(755,root,root) %ghost %{_libdir}/libkopetestatusmenu.so.1
%attr(755,root,root) %{_libdir}/libkopetestatusmenu.so.1.*.*
%attr(755,root,root) %ghost %{_libdir}/liboscar.so.1
%attr(755,root,root) %{_libdir}/liboscar.so.1.*.*
%attr(755,root,root) %{_libdir}/libqgroupwise.so
# TODO proper package for this dir
%dir %{_libdir}/qt5/plugins/accessible
%attr(755,root,root) %{_libdir}/qt5/plugins/accessible/chatwindowaccessiblewidgetfactory.so
%attr(755,root,root) %{_libdir}/qt5/plugins/chattexteditpart.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_kopete_accountconfig.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_kopete_addbookmarks.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_kopete_appearanceconfig.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_kopete_autoreplace.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_kopete_avdeviceconfig.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_kopete_behaviorconfig.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_kopete_chatwindowconfig.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_kopete_highlight.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_kopete_history.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_kopete_pluginconfig.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_kopete_privacy.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_kopete_statusconfig.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_kopete_texteffect.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_kopete_urlpicpreview.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_kopete_webpresence.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kopete_addbookmarks.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kopete_aim.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kopete_autoreplace.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kopete_bonjour.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kopete_chatwindow.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kopete_contactnotes.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kopete_emailwindow.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kopete_groupwise.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kopete_highlight.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kopete_history.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kopete_icq.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kopete_jabber.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kopete_privacy.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kopete_qq.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kopete_statistics.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kopete_testbed.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kopete_texteffect.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kopete_urlpicpreview.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kopete_webpresence.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kopete_wp.so
%{_desktopdir}/org.kde.kopete.desktop
%{_datadir}/config.kcfg/historyconfig.kcfg
%{_datadir}/config.kcfg/kopeteappearancesettings.kcfg
%{_datadir}/config.kcfg/kopetebehaviorsettings.kcfg
%{_datadir}/config.kcfg/kopetestatussettings.kcfg
%{_datadir}/config.kcfg/urlpicpreview.kcfg
%{_datadir}/config.kcfg/webpresenceconfig.kcfg
%{_datadir}/dbus-1/interfaces/org.kde.Kopete.xml
%{_datadir}/dbus-1/interfaces/org.kde.kopete.Client.xml
%{_datadir}/dbus-1/interfaces/org.kde.kopete.Statistics.xml
%{_iconsdir}/hicolor/128x128/apps/kopete-offline.png
%{_iconsdir}/hicolor/128x128/apps/kopete.png
%{_iconsdir}/hicolor/16x16/apps/kopete-offline.png
%{_iconsdir}/hicolor/16x16/apps/kopete.png
%{_iconsdir}/hicolor/22x22/apps/kopete-offline.png
%{_iconsdir}/hicolor/22x22/apps/kopete.png
%{_iconsdir}/hicolor/32x32/apps/kopete-offline.png
%{_iconsdir}/hicolor/32x32/apps/kopete.png
%{_iconsdir}/hicolor/48x48/apps/kopete-offline.png
%{_iconsdir}/hicolor/48x48/apps/kopete.png
%{_iconsdir}/hicolor/64x64/apps/kopete-offline.png
%{_iconsdir}/hicolor/64x64/apps/kopete.png
%{_iconsdir}/hicolor/scalable/apps/kopete-offline.svgz
%{_iconsdir}/hicolor/scalable/apps/kopete.svgz
%{_iconsdir}/oxygen/128x128/actions/voicecall.png
%{_iconsdir}/oxygen/128x128/actions/webcamreceive.png
%{_iconsdir}/oxygen/128x128/actions/webcamsend.png
%{_iconsdir}/oxygen/128x128/apps/kopete_avdevice.png
%{_iconsdir}/oxygen/16x16/actions/account_offline_overlay.png
%{_iconsdir}/oxygen/16x16/actions/contact_away_overlay.png
%{_iconsdir}/oxygen/16x16/actions/contact_busy_overlay.png
%{_iconsdir}/oxygen/16x16/actions/contact_food_overlay.png
%{_iconsdir}/oxygen/16x16/actions/contact_freeforchat_overlay.png
%{_iconsdir}/oxygen/16x16/actions/contact_invisible_overlay.png
%{_iconsdir}/oxygen/16x16/actions/contact_phone_overlay.png
%{_iconsdir}/oxygen/16x16/actions/contact_xa_overlay.png
%{_iconsdir}/oxygen/16x16/actions/emoticon.png
%{_iconsdir}/oxygen/16x16/actions/im-status-message-edit.png
%{_iconsdir}/oxygen/16x16/actions/metacontact_unknown.png
%{_iconsdir}/oxygen/16x16/actions/status_unknown.png
%{_iconsdir}/oxygen/16x16/actions/status_unknown_overlay.png
%{_iconsdir}/oxygen/16x16/actions/view-user-offline-kopete.png
%{_iconsdir}/oxygen/16x16/actions/voicecall.png
%{_iconsdir}/oxygen/16x16/actions/webcamreceive.png
%{_iconsdir}/oxygen/16x16/actions/webcamsend.png
%{_iconsdir}/oxygen/22x22/actions/account_offline_overlay.png
%{_iconsdir}/oxygen/22x22/actions/im-status-message-edit.png
%{_iconsdir}/oxygen/22x22/actions/view-user-offline-kopete.png
%{_iconsdir}/oxygen/22x22/actions/voicecall.png
%{_iconsdir}/oxygen/22x22/actions/webcamreceive.png
%{_iconsdir}/oxygen/22x22/actions/webcamsend.png
%{_iconsdir}/oxygen/22x22/apps/kopete_avdevice.png
%{_iconsdir}/oxygen/32x32/actions/account_offline_overlay.png
%{_iconsdir}/oxygen/32x32/actions/im-status-message-edit.png
%{_iconsdir}/oxygen/32x32/actions/metacontact_unknown.png
%{_iconsdir}/oxygen/32x32/actions/view-user-offline-kopete.png
%{_iconsdir}/oxygen/32x32/actions/voicecall.png
%{_iconsdir}/oxygen/32x32/actions/webcamreceive.png
%{_iconsdir}/oxygen/32x32/actions/webcamsend.png
%{_iconsdir}/oxygen/32x32/apps/kopete_avdevice.png
%{_iconsdir}/oxygen/48x48/actions/im-status-message-edit.png
%{_iconsdir}/oxygen/48x48/actions/view-user-offline-kopete.png
%{_iconsdir}/oxygen/48x48/actions/voicecall.png
%{_iconsdir}/oxygen/48x48/actions/webcamreceive.png
%{_iconsdir}/oxygen/48x48/actions/webcamsend.png
%{_iconsdir}/oxygen/64x64/actions/voicecall.png
%{_iconsdir}/oxygen/64x64/actions/webcamreceive.png
%{_iconsdir}/oxygen/64x64/actions/webcamsend.png
%{_iconsdir}/oxygen/64x64/apps/kopete_avdevice.png
%{_iconsdir}/oxygen/scalable/actions/account_offline_overlay.svgz
%{_iconsdir}/oxygen/scalable/actions/im-status-message-edit.svgz
%{_iconsdir}/oxygen/scalable/actions/view-user-offline-kopete.svgz
%{_iconsdir}/oxygen/scalable/actions/voicecall.svgz
%{_iconsdir}/oxygen/scalable/actions/webcamreceive.svgz
%{_iconsdir}/oxygen/scalable/actions/webcamsend.svgz
%attr(755,root,root) %{_datadir}/kconf_update/kopete-account-0.10.pl
%attr(755,root,root) %{_datadir}/kconf_update/kopete-account-kconf_update.sh
%{_datadir}/kconf_update/kopete-account-kconf_update.upd
%attr(755,root,root) %{_datadir}/kconf_update/kopete-gaim_to_pidgin_style.pl
%{_datadir}/kconf_update/kopete-gaim_to_pidgin_style.upd
%attr(755,root,root) %{_datadir}/kconf_update/kopete-initialstatus.pl
%{_datadir}/kconf_update/kopete-initialstatus.upd
%attr(755,root,root) %{_datadir}/kconf_update/kopete-jabberpriorityaddition-kconf_update.sh
%{_datadir}/kconf_update/kopete-jabberpriorityaddition-kconf_update.upd
%attr(755,root,root) %{_datadir}/kconf_update/kopete-jabberproxytype-kconf_update.sh
%{_datadir}/kconf_update/kopete-jabberproxytype-kconf_update.upd
%{_datadir}/kconf_update/kopete-nameTracking.upd
%attr(755,root,root) %{_datadir}/kconf_update/kopete-pluginloader.pl
%{_datadir}/kconf_update/kopete-pluginloader.upd
%attr(755,root,root) %{_datadir}/kconf_update/kopete-pluginloader2.sh
%{_datadir}/kconf_update/kopete-pluginloader2.upd
%attr(755,root,root) %{_datadir}/kconf_update/kopete-update_icq_server.pl
%{_datadir}/kconf_update/kopete-update_icq_server.upd
%attr(755,root,root) %{_datadir}/kconf_update/kopete-update_icq_ssl.pl
%{_datadir}/kconf_update/kopete-update_icq_ssl.upd
%{_datadir}/knotifications5/kopete.notifyrc
%{_datadir}/kopete
%{_datadir}/kopete_history
%{_datadir}/kservices5/aim.protocol
%{_datadir}/kservices5/chatwindow.desktop
%{_datadir}/kservices5/emailwindow.desktop
%dir %{_datadir}/kservices5/kconfiguredialog
%{_datadir}/kservices5/kconfiguredialog/kopete_addbookmarks_config.desktop
%{_datadir}/kservices5/kconfiguredialog/kopete_autoreplace_config.desktop
%{_datadir}/kservices5/kconfiguredialog/kopete_highlight_config.desktop
%{_datadir}/kservices5/kconfiguredialog/kopete_history_config.desktop
%{_datadir}/kservices5/kconfiguredialog/kopete_privacy_config.desktop
%{_datadir}/kservices5/kconfiguredialog/kopete_texteffect_config.desktop
%{_datadir}/kservices5/kconfiguredialog/kopete_urlpicpreview_config.desktop
%{_datadir}/kservices5/kconfiguredialog/kopete_webpresence_config.desktop
%{_datadir}/kservices5/kopete_accountconfig.desktop
%{_datadir}/kservices5/kopete_addbookmarks.desktop
%{_datadir}/kservices5/kopete_aim.desktop
%{_datadir}/kservices5/kopete_appearanceconfig.desktop
%{_datadir}/kservices5/kopete_autoreplace.desktop
%{_datadir}/kservices5/kopete_avdeviceconfig.desktop
%{_datadir}/kservices5/kopete_behaviorconfig.desktop
%{_datadir}/kservices5/kopete_bonjour.desktop
%{_datadir}/kservices5/kopete_chatwindowconfig.desktop
%{_datadir}/kservices5/kopete_contactnotes.desktop
%{_datadir}/kservices5/kopete_groupwise.desktop
%{_datadir}/kservices5/kopete_highlight.desktop
%{_datadir}/kservices5/kopete_history.desktop
%{_datadir}/kservices5/kopete_icq.desktop
%{_datadir}/kservices5/kopete_jabber.desktop
%{_datadir}/kservices5/kopete_pluginconfig.desktop
%{_datadir}/kservices5/kopete_privacy.desktop
%{_datadir}/kservices5/kopete_qq.desktop
%{_datadir}/kservices5/kopete_statistics.desktop
%{_datadir}/kservices5/kopete_statusconfig.desktop
%{_datadir}/kservices5/kopete_testbed.desktop
%{_datadir}/kservices5/kopete_texteffect.desktop
%{_datadir}/kservices5/kopete_urlpicpreview.desktop
%{_datadir}/kservices5/kopete_webpresence.desktop
%{_datadir}/kservices5/kopete_wp.desktop
%{_datadir}/kservices5/xmpp.protocol
%{_datadir}/kservicetypes5/kopeteplugin.desktop
%{_datadir}/kservicetypes5/kopeteprotocol.desktop
%{_datadir}/kservicetypes5/kopeteui.desktop
%{_datadir}/kxmlgui5/kopete
%{_datadir}/kxmlgui5/kopete_groupwise
%{_datadir}/metainfo/org.kde.kopete.appdata.xml
%{_datadir}/sounds/Kopete_Event.ogg
%{_datadir}/sounds/Kopete_Received.ogg
%{_datadir}/sounds/Kopete_Sent.ogg
%{_datadir}/sounds/Kopete_User_is_Online.ogg
%{_datadir}/qlogging-categories5/kopete.categories

%ghost %{_libdir}/libkopete_otr_shared.so.1
%{_libdir}/libkopete_otr_shared.so.1.*.*
%{_libdir}/qt5/plugins/kcm_kopete_otr.so
%{_libdir}/qt5/plugins/kopete_otr.so
%{_datadir}/config.kcfg/kopete_otr.kcfg
%{_iconsdir}/oxygen/22x22/status/object-locked-finished.png
%{_iconsdir}/oxygen/22x22/status/object-locked-unverified.png
%{_iconsdir}/oxygen/22x22/status/object-locked-verified.png
%{_iconsdir}/oxygen/48x48/actions/mail-encrypt.png
%{_datadir}/kservices5/kconfiguredialog/kopete_otr_config.desktop
%{_datadir}/kservices5/kopete_otr.desktop
%{_datadir}/kxmlgui5/kopete_otr/otrchatui.rc
%{_datadir}/kxmlgui5/kopete_otr/otrui.rc

%files devel
%defattr(644,root,root,755)
%{_includedir}/kopete
%attr(755,root,root) %{_libdir}/libkopete.so
%attr(755,root,root) %{_libdir}/libkopete_oscar.so
%attr(755,root,root) %{_libdir}/libkopete_videodevice.so
%attr(755,root,root) %{_libdir}/libkopeteaddaccountwizard.so
%attr(755,root,root) %{_libdir}/libkopetechatwindow_shared.so
%attr(755,root,root) %{_libdir}/libkopetecontactlist.so
%attr(755,root,root) %{_libdir}/libkopeteidentity.so
%attr(755,root,root) %{_libdir}/libkopeteprivacy.so
%attr(755,root,root) %{_libdir}/libkopetestatusmenu.so
%attr(755,root,root) %{_libdir}/liboscar.so
%{_libdir}/libkopete_otr_shared.so
