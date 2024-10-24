<%@ page import="java.sql.*" %>
<html>
<body>
<h2>Prueba de conexión MySQL</h2>
<%
    String url = "jdbc:mysql://mysql:3306/testdb";
    String username = "root";
    String password = "secret";

    Connection conn = null;
    Statement stmt = null;
    ResultSet rs = null;

    try {
        Class.forName("com.mysql.cj.jdbc.Driver");
        conn = DriverManager.getConnection(url, username, password);
        stmt = conn.createStatement();
        rs = stmt.executeQuery("SELECT 'Conexión Exitosa' as resultado FROM DUAL");

        while(rs.next()) {
            out.println("Resultado: " + rs.getString("resultado") + "<br>");
        }
    } catch (Exception e) {
        out.println("Error: " + e.getMessage() + "<br>");
    } finally {
        try { if (rs != null) rs.close(); } catch (SQLException e) { }
        try { if (stmt != null) stmt.close(); } catch (SQLException e) { }
        try { if (conn != null) conn.close(); } catch (SQLException e) { }
    }
%>
</body>
</html>
