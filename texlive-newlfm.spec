Name:		texlive-newlfm
Version:	15878
Release:	2
Summary:	Write letters, facsimiles, and memos
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/newlfm
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newlfm.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newlfm.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newlfm.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Integrates the letter class with fancyhdr and geometry to
automatically make letterhead stationery. Useful for writing
letters, fax, and memos. You can set up an address book using
'wrapper' macros. You put all the information for a person into
a wrapper and then put the wrapper in a document. The class
handles letterheads automatically. You place the object for the
letterhead (picture, information, etc.) in a box and all sizing
is set automatically.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/newlfm/addrset.sty
%{_texmfdistdir}/tex/latex/newlfm/newlfm.cls
%{_texmfdistdir}/tex/latex/newlfm/setdim.sty
%doc %{_texmfdistdir}/doc/latex/newlfm/README
%doc %{_texmfdistdir}/doc/latex/newlfm/chk1.tex
%doc %{_texmfdistdir}/doc/latex/newlfm/demoa.tex
%doc %{_texmfdistdir}/doc/latex/newlfm/draft.eps
%doc %{_texmfdistdir}/doc/latex/newlfm/draft.pdf
%doc %{_texmfdistdir}/doc/latex/newlfm/extracd.tex
%doc %{_texmfdistdir}/doc/latex/newlfm/hletrinf.tex
%doc %{_texmfdistdir}/doc/latex/newlfm/letrinfo.tex
%doc %{_texmfdistdir}/doc/latex/newlfm/lvb.eps
%doc %{_texmfdistdir}/doc/latex/newlfm/lvb.pdf
%doc %{_texmfdistdir}/doc/latex/newlfm/make_clean
%doc %{_texmfdistdir}/doc/latex/newlfm/make_unix
%doc %{_texmfdistdir}/doc/latex/newlfm/make_win.bat
%doc %{_texmfdistdir}/doc/latex/newlfm/makeclean_win.bat
%doc %{_texmfdistdir}/doc/latex/newlfm/manual.pdf
%doc %{_texmfdistdir}/doc/latex/newlfm/mintrx.bat
%doc %{_texmfdistdir}/doc/latex/newlfm/newlfm.pdf
%doc %{_texmfdistdir}/doc/latex/newlfm/newlfm.txt
%doc %{_texmfdistdir}/doc/latex/newlfm/palm.eps
%doc %{_texmfdistdir}/doc/latex/newlfm/palm.pdf
%doc %{_texmfdistdir}/doc/latex/newlfm/problems.tex
%doc %{_texmfdistdir}/doc/latex/newlfm/prx.bat
%doc %{_texmfdistdir}/doc/latex/newlfm/setup.bat
%doc %{_texmfdistdir}/doc/latex/newlfm/sfaxpage.tex
%doc %{_texmfdistdir}/doc/latex/newlfm/smemosec.tex
%doc %{_texmfdistdir}/doc/latex/newlfm/sprsrls.tex
%doc %{_texmfdistdir}/doc/latex/newlfm/test1.tex
%doc %{_texmfdistdir}/doc/latex/newlfm/test10.tex
%doc %{_texmfdistdir}/doc/latex/newlfm/test11.tex
%doc %{_texmfdistdir}/doc/latex/newlfm/test12.tex
%doc %{_texmfdistdir}/doc/latex/newlfm/test1alt.tex
%doc %{_texmfdistdir}/doc/latex/newlfm/test2.tex
%doc %{_texmfdistdir}/doc/latex/newlfm/test2a.tex
%doc %{_texmfdistdir}/doc/latex/newlfm/test2alt.tex
%doc %{_texmfdistdir}/doc/latex/newlfm/test3.tex
%doc %{_texmfdistdir}/doc/latex/newlfm/test3alt.tex
%doc %{_texmfdistdir}/doc/latex/newlfm/test4.tex
%doc %{_texmfdistdir}/doc/latex/newlfm/test4alt.tex
%doc %{_texmfdistdir}/doc/latex/newlfm/test5.tex
%doc %{_texmfdistdir}/doc/latex/newlfm/test5alt.tex
%doc %{_texmfdistdir}/doc/latex/newlfm/test6.tex
%doc %{_texmfdistdir}/doc/latex/newlfm/test6alt.tex
%doc %{_texmfdistdir}/doc/latex/newlfm/test7.tex
%doc %{_texmfdistdir}/doc/latex/newlfm/test7alt.tex
%doc %{_texmfdistdir}/doc/latex/newlfm/test8.tex
%doc %{_texmfdistdir}/doc/latex/newlfm/test8alt.tex
%doc %{_texmfdistdir}/doc/latex/newlfm/test9.tex
%doc %{_texmfdistdir}/doc/latex/newlfm/testms.pdf
%doc %{_texmfdistdir}/doc/latex/newlfm/wine.eps
%doc %{_texmfdistdir}/doc/latex/newlfm/wine.pdf
#- source
%doc %{_texmfdistdir}/source/latex/newlfm/newlfm.dtx
%doc %{_texmfdistdir}/source/latex/newlfm/newlfm.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
