Summary: OpenAL Soft
Name: OpenAL
Version: 1.24.3
Release: 1
Source: %{name}-%{version}.tar.bz2
URL: https://github.com/sailfishos/libopenal
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
%cmake \
    -DALSOFT_REQUIRE_PULSEAUDIO=ON \
    -DALSOFT_BACKEND_ALSA=OFF \
    -DALSOFT_BACKEND_OSS=OFF \
    -DALSOFT_BACKEND_SDL2=OFF \
    -DALSOFT_NO_CONFIG_UTIL=ON \
    -DALSOFT_EXAMPLES=ON
%cmake_build

%install
%cmake_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING BSD-3Clause
%doc README.md docs/env-vars.txt docs/hrtf.txt
%{_bindir}/openal-info
%{_libdir}/lib*.so.*
%{_datadir}/openal/*

%files devel
%{_libdir}/lib*.so
%{_includedir}/*/*.h
%{_libdir}/pkgconfig/*
%{_libdir}/cmake/OpenAL

%files tests
%{_bindir}/al*
