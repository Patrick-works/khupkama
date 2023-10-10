<%@ Page Title="Home Page" Language="C#" MasterPageFile="~/Site.master" AutoEventWireup="true"
    CodeFile="Default.aspx.cs" Inherits="_Default" %>

<asp:Content ID="HeaderContent" runat="server" ContentPlaceHolderID="HeadContent">
</asp:Content>
<asp:Content ID="BodyContent" runat="server" ContentPlaceHolderID="MainContent">
    <h2>
        Welcome to ASP.NET!
    </h2>
    <p>
        To learn more about ASP.NET visit <a href="http://www.asp.net" title="ASP.NET Website">www.asp.net</a>.
    </p>
    <p>
        You can also find <a href="http://go.microsoft.com/fwlink/?LinkID=152368&amp;clcid=0x409"
            title="MSDN ASP.NET Docs">documentation on ASP.NET at MSDN</a>.
    </p>
<p>
        <asp:GridView ID="GridView1" runat="server" AutoGenerateColumns="False" 
            DataSourceID="SqlDataSource1" 
            onselectedindexchanged="GridView1_SelectedIndexChanged">
            <Columns>
                <asp:BoundField DataField="Rollno" HeaderText="Rollno" 
                    SortExpression="Rollno" />
                <asp:BoundField DataField="name" HeaderText="name" SortExpression="name" />
                <asp:CommandField HeaderText="Delete" ShowDeleteButton="True" 
                    ShowHeader="True" />
                <asp:CommandField ShowEditButton="True" />
                <asp:CommandField ShowEditButton="True" />
            </Columns>
        </asp:GridView>
        <asp:SqlDataSource ID="SqlDataSource1" runat="server" 
            ConnectionString="<%$ ConnectionStrings:masterStudConnectionString %>" 
            SelectCommand="SELECT * FROM [students]"
            DeleteCommand ="delete from [students] where [Rollno]= @Rollno"
            UpdateCommand="UPDATE students SET Rollno = @Rollno, name = @name WHERE (Rollno = @Rollno)"
            
            ConflictDetection="CompareAllValues">
            </asp:SqlDataSource>
            
    </p>
</asp:Content>
