# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       gfx-rpi

# >> macros
# << macros

Summary:    VideoCore libraries for Raspberry Pi
Version:    0.0.4
Release:    1
Group:      System/Libraries
License:    Broadcom Proprietary
URL:        https://github.com/cxl000/mer-rapberrypi-userland/
Source0:    %{name}-%{version}.tar.bz2
Source1:    mer-arm-linux.cmake
Source2:    prebuilt.tar.bz2
Source3:    egl.pc
Source4:    glesv1_cm.pc
Source5:    glesv2.pc
Source6:    omxil.pc
Source7:    bcm_host.pc
Source100:  gfx-rpi.yaml
Patch0:     gfx-rpi-not-all-apps.patch
Requires(post): /sbin/service
Requires(post): /sbin/chkconfig
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/service
Requires(postun): /sbin/chkconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  cmake

%description
Broadcom VideoCore Linux libraries for Raspberry Pi
This package contains the common binaries and libraries.


%package devel
Summary:    Common devel files for RaspberryPi Broadcom VideoCore
Group:      Development/System
Requires:   %{name} = %{version}-%{release}

%description devel
Headers for common RaspberryPi Broadcom VideoCore.


%package libOMXIL
Summary:    OMX IL for Broadcom VideoCore
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides:   libOMXIL
Provides:   libopenmaxil.so

%description libOMXIL
This package provides OMX IL library for Broadcom VideoCore


%package libOMXIL-devel
Summary:    OMX IL development headers for Broadcom VideoCore
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   %{name}-libOMXIL = %{version}-%{release}
Provides:   libOMXIL-devel

%description libOMXIL-devel
This package provides OMXIL headers for Broadcom VideoCore.


%package libEGL
Summary:    EGL for Broadcom VideoCore
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides:   libEGL
Provides:   libEGL.so.1

%description libEGL
This package provides EGL library for Broadcom VideoCore


%package libEGL-devel
Summary:    EGL development headers for Broadcom VideoCore
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   %{name}-libEGL = %{version}-%{release}
Provides:   libEGL-devel

%description libEGL-devel
This package provides EGL headers for Broadcom VideoCore.


%package libGLESv1
Summary:    GLESv1 for Broadcom VideoCore
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides:   libGLESv1
Provides:   libGLES_CM.so.1

%description libGLESv1
This package provides OpenGL ES v1 libraries for Broadcom VideoCore.


%package libGLESv1-devel
Summary:    GLESv1 development headers for Broadcom VideoCore
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   %{name}-libGLESv1 = %{version}-%{release}
Provides:   libGLESv1-devel

%description libGLESv1-devel
This package provides OpenGL ES v1 headers for Broadcom VideoCore.


%package libGLESv2
Summary:    GLESv2 for Broadcom VideoCore
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides:   libGLESv2
Provides:   libGLESv2.so.2

%description libGLESv2
This package provides OpenGL ES v2 libraries for Broadcom VideoCore.


%package libGLESv2-devel
Summary:    GLESv2 development headers for Broadcom VideoCore
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   %{name}-libGLESv2 = %{version}-%{release}
Provides:   libGLESv2-devel

%description libGLESv2-devel
This package provides OpenGL ES v2 headers for Broadcom VideoCore.


%package test
Summary:    Test programs for Broadcom VideoCore
Group:      Development/Tools
Requires:   %{name} = %{version}-%{release}

%description test
This package provides test programs for Broadcom VideoCore.


%package examples
Summary:    Example source for Broadcom VideoCore test programs
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description examples
This package provides example source for Broadcom VideoCore test programs.


%prep
%setup -q -n %{name}-%{version}/userland
tar xvf %{SOURCE2}

# gfx-rpi-not-all-apps.patch
%patch0 -p1
# >> setup
# << setup

%build
# >> build pre
# << build pre

%cmake .  \
    -DCMAKE_TOOLCHAIN_FILE=%{SOURCE1} \
    -DENABLE_3D_TESTS:BOOL=ON \
    -DALL_APPS:BOOL=ON

make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
mkdir -p %{buildroot}/%{_prefix}
mv %{buildroot}/opt/vc/* %{buildroot}/%{_prefix}/

rm -rf %{buildroot}/%{_prefix}/src/hello_pi/hello_videocube/CMakeFiles
rm -rf %{buildroot}/%{_prefix}/src/hello_pi/hello_world/CMakeFiles
rm %{buildroot}/%{_prefix}/src/hello_pi/hello_videocube/cmake_install.cmake
rm %{buildroot}/%{_prefix}/src/hello_pi/hello_world/Makefile
rm %{buildroot}/%{_prefix}/src/hello_pi/hello_world/cmake_install.cmake
rm %{buildroot}/%{_prefix}/src/hello_pi/libs/ilclient/Makefile
rm %{buildroot}/%{_prefix}/src/hello_pi/libs/vgfont/Makefile

%ifarch armv6hl
#cp -av armv6hl/libGLESv1_CM.so %{buildroot}/%{_libdir}/
#chmod 0755 %{buildroot}/%{_libdir}/libGLESv1_CM.so
%endif
%ifarch armv6l
#cp -av armv6l/libGLESv1_CM.so %{buildroot}/%{_libdir}/
#chmod 0755 %{buildroot}/%{_libdir}/libGLESv1_CM.so
%endif

ln -s libEGL.so %{buildroot}/%{_libdir}/libEGL.so.1
#ln -s libGLESv1_CM.so %{buildroot}/%{_libdir}/libGLESv1_CM.so.1
ln -s libGLESv2.so %{buildroot}/%{_libdir}/libGLESv2.so.2

mkdir -p %{buildroot}/%{_docdir}/
mv LICENCE %{buildroot}/%{_docdir}/LICENCE

mkdir -p %{buildroot}/%{_libdir}/pkgconfig
cp %{SOURCE3} %{buildroot}/%{_libdir}/pkgconfig/
cp %{SOURCE4} %{buildroot}/%{_libdir}/pkgconfig/
cp %{SOURCE5} %{buildroot}/%{_libdir}/pkgconfig/
cp %{SOURCE6} %{buildroot}/%{_libdir}/pkgconfig/
cp %{SOURCE7} %{buildroot}/%{_libdir}/pkgconfig/
# << install post

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post libOMXIL -p /sbin/ldconfig

%postun libOMXIL -p /sbin/ldconfig

%post libEGL -p /sbin/ldconfig

%postun libEGL -p /sbin/ldconfig

%post libGLESv1 -p /sbin/ldconfig

%postun libGLESv1 -p /sbin/ldconfig

%post libGLESv2 -p /sbin/ldconfig

%postun libGLESv2 -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc %{_docdir}/LICENCE
%{_bindir}/vcgencmd
%{_bindir}/vchiq_test
%{_bindir}/tvservice
%{_bindir}/raspistill
%{_bindir}/raspivid
%{_bindir}/raspiyuv
%{_sbindir}/vcfiled
%{_libdir}/libmmal.so
%{_libdir}/libmmal_core.so
%{_libdir}/libmmal_util.so
%{_libdir}/libmmal_vc_client.so
%{_libdir}/libWFC.so
%{_libdir}/libOpenVG.so
%{_libdir}/libvcos.so
%{_libdir}/libvchiq_arm.so
%{_libdir}/libbcm_host.so
%{_libdir}/libkhrn_client.so
%{_libdir}/libvcfiled_check.so
%{_libdir}/libvchostif.so
%{_libdir}/libvmcs_rpc_client.so
%{_dataddir}/install/vcfiled
# >> files
%{_initddir}/vcfiled
#%{_bindir}/vcdbg
#%{_bindir}/edidparser
#%{_bindir}/mmal_vc_diag
#%{_libdir}/libdebug_sym.so
# << files

%files devel
%defattr(-,root,root,-)
%doc %{_docdir}/LICENCE
%{_includedir}/interface
%{_includedir}/vcinclude
%{_includedir}/VG
%{_includedir}/WF
%{_includedir}/bcm_host.h
# >> files devel
# << files devel

%files libOMXIL
%defattr(-,root,root,-)
%doc %{_docdir}/LICENCE
%{_libdir}/libopenmaxil.so
# >> files libOMXIL
# << files libOMXIL

%files libOMXIL-devel
%defattr(-,root,root,-)
%doc %{_docdir}/LICENCE
%{_includedir}/IL/*.h
%{_libdir}/pkgconfig/omxil.pc
# >> files libOMXIL-devel
# << files libOMXIL-devel

%files libEGL
%defattr(-,root,root,-)
%{_libdir}/libEGL.so*
# >> files libEGL
# << files libEGL

%files libEGL-devel
%defattr(-,root,root,-)
%{_includedir}/KHR/*.h
%{_includedir}/EGL/*.h
%{_libdir}/pkgconfig/egl.pc
%{_libdir}/pkgconfig/bcm_host.pc
# >> files libEGL-devel
# << files libEGL-devel

%files libGLESv1
%defattr(-,root,root,-)
%doc %{_docdir}/LICENCE
#%{_libdir}/libGLESv1_CM.so*
# >> files libGLESv1
# << files libGLESv1

%files libGLESv1-devel
%defattr(-,root,root,-)
%doc %{_docdir}/LICENCE
%{_includedir}/GLES/*.h
%{_libdir}/pkgconfig/glesv1_cm.pc
# >> files libGLESv1-devel
# << files libGLESv1-devel

%files libGLESv2
%defattr(-,root,root,-)
%doc %{_docdir}/LICENCE
%{_libdir}/libGLESv2.so*
# >> files libGLESv2
# << files libGLESv2

%files libGLESv2-devel
%defattr(-,root,root,-)
%doc %{_docdir}/LICENCE
%{_includedir}/GLES2/*.h
%{_libdir}/pkgconfig/glesv2.pc
# >> files libGLESv2-devel
# << files libGLESv2-devel

%files test
%defattr(-,root,root,-)
%{_bindir}/hello_audio.bin
%{_bindir}/hello_dispmanx.bin
%{_bindir}/hello_encode.bin
%{_bindir}/hello_jpeg.bin
%{_bindir}/hello_teapot.bin
%{_bindir}/hello_tiger.bin
%{_bindir}/hello_triangle.bin
%{_bindir}/hello_triangle2.bin
%{_bindir}/hello_video.bin
%{_bindir}/hello_videocube.bin
%{_bindir}/hello_world.bin
# >> files test
# << files test

%files examples
%defattr(-,root,root,-)
%{_prefix}/src/hello_pi
# >> files examples
# << files examples