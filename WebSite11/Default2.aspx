<%@ Page Title="" Language="C#" MasterPageFile="~/Site.master" Theme="Theme1" AutoEventWireup="true" CodeFile="Default2.aspx.cs" Inherits="Default2" %>

<asp:Content ID="Content1" ContentPlaceHolderID="HeadContent" Runat="Server">
</asp:Content>
<asp:Content ID="Content2" ContentPlaceHolderID="MainContent" Runat="Server">
    <asp:Label ID="Label1" runat="server" SkindId="lbl" Text="Label"></asp:Label>
    <asp:Calendar ID="Calendar1" runat="server"></asp:Calendar>
    <asp:HyperLink ID="HyperLink1" runat="server" NavigateUrl="~/Default5.aspx">HyperLink</asp:HyperLink>
</asp:Content>

