%global tl_name newlfm
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	9.4
Release:	%{tl_revision}.1
Summary:	Write letters, facsimiles, and memos
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/newlfm
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/newlfm.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/newlfm.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/newlfm.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Integrates the letter class with fancyhdr and geometry to automatically
make letterhead stationery. Useful for writing letters, fax, and memos.
You can set up an address book using 'wrapper' macros. You put all the
information for a person into a wrapper and then put the wrapper in a
document. The class handles letterheads automatically. You place the
object for the letterhead (picture, information, etc.) in a box and all
sizing is set automatically.

