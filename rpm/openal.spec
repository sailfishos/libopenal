Summary: OpenAL Soft
Name: OpenAL
Version: 1.23.1
Release: 1
Source: %{name}-%{version}.tar.bz2
URL: https://www.openal-soft.org/
License: LGPLv2+ and BSD-3-Clause
BuildRequires: cmake
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(sdl2)
BuildRequires: pkgconfig(sndfile)
BuildRequires: SDL2_sound-devel


%description
OpenAL provides capabilities for playing audio in a virtual 3D environment.
Distance attenuation, doppler shift, and directional sound emitters are among
the features handled by the API. More advanced effects, including air
absorption, occlusion, and environmental reverb, are available through the EFX
extension. It also facilitates streaming audio, multi-channel buffers, and
audio capture.

%package devel
Summary: OpenAL Soft - Development libraries
Requires: %{name} = %{version}

%description devel
OpenAL provides capabilities for playing audio in a virtual 3D environment.
Distance attenuation, doppler shift, and directional sound emitters are among
the features handled by the API. More advanced effects, including air
absorption, occlusion, and environmental reverb, are available through the EFX
extension. It also facilitates streaming audio, multi-channel buffers, and
audio capture.

%package tests
Summary: OpenAL Soft - Test applications
Requires: %{name} = %{version}

%description tests
OpenAL provides capabilities for playing audio in a virtual 3D environment.
Distance attenuation, doppler shift, and directional sound emitters are among
the features handled by the API. More advanced effects, including air
absorption, occlusion, and environmental reverb, are available through the EFX
extension. It also facilitates streaming audio, multi-channel buffers, and
audio capture.


%prep
%autosetup -n %{name}-%{version}/upstream

%build
pushd build
%cmake .. \
    -DALSOFT_REQUIRE_PULSEAUDIO=ON \
    -DALSOFT_BACKEND_ALSA=OFF \
    -DALSOFT_BACKEND_OSS=OFF \
    -DALSOFT_BACKEND_SDL2=OFF \
    -DALSOFT_EXAMPLES=ON
%make_build
popd

%install
pushd build
%make_install
popd

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license COPYING BSD-3Clause
%doc README.md docs/env-vars.txt docs/hrtf.txt
%{_bindir}/openal-info
%{_libdir}/lib*.so.*
%{_datadir}/openal/*

%files devel
%defattr(-,root,root,-)
%{_libdir}/lib*.so
%{_includedir}/*/*.h
%{_libdir}/pkgconfig/*
%{_libdir}/cmake/OpenAL

%files tests
%defattr(-,root,root,-)
%{_bindir}/al*
