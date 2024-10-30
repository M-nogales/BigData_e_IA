package com.ejemplo;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.Statement;

import javax.servlet.annotation.WebServlet;

@WebServlet(name = "App", urlPatterns = {"/", "/addUser"})
public class App extends HttpServlet {

    private static final String DB_URL = "jdbc:mysql://db:3306/mi_base_datos";
    private static final String USER = "mi_usuario";
    private static final String PASS = "mi_contraseña";

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();

        Connection conn = null;
        Statement stmt = null;

        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            conn = DriverManager.getConnection(DB_URL, USER, PASS);

            // Verificar si la tabla 'usuarios' existe, si no existe crearla
            stmt = conn.createStatement();
            String createTableSQL = "CREATE TABLE IF NOT EXISTS usuarios ("
                + "id INT AUTO_INCREMENT PRIMARY KEY, "
                + "nombre VARCHAR(50) NOT NULL, "
                + "email VARCHAR(100) NOT NULL UNIQUE, "
                + "contrasena VARCHAR(255) NOT NULL, "
                + "fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP);";
            stmt.execute(createTableSQL);

            // Verificar si la tabla está vacía y si es así, insertar datos predeterminados
            String countSQL = "SELECT COUNT(*) FROM usuarios;";
            ResultSet rsCount = stmt.executeQuery(countSQL);
            if (rsCount.next() && rsCount.getInt(1) == 0) {
                String insertSQL = "INSERT INTO usuarios (nombre, email, contrasena) VALUES (?, ?, ?)";
                try (PreparedStatement pstmt = conn.prepareStatement(insertSQL)) {
                    // Datos predeterminados
                    String[][] usuarios = {
                        {"Juan Pérez", "juan.perez@example.com", "contrasena123"},
                        {"María García", "maria.garcia@example.com", "secreta456"},
                        {"Luis Rodríguez", "luis.rodriguez@example.com", "miClave789"},
                        {"Ana López", "ana.lopez@example.com", "password321"},
                        {"Carlos Torres", "carlos.torres@example.com", "12345678"}
                    };
                    for (String[] usuario : usuarios) {
                        pstmt.setString(1, usuario[0]);
                        pstmt.setString(2, usuario[1]);
                        pstmt.setString(3, usuario[2]);
                        pstmt.executeUpdate();
                    }
                }
            }

            // Leer usuarios de la base de datos
            String sql = "SELECT * FROM usuarios";
            ResultSet rs = stmt.executeQuery(sql);

            // HTML response
            out.println("<html><head><title>Usuarios</title>");
            out.println("<style>");
            out.println("table { width: 100%; border-collapse: collapse; }");
            out.println("th, td { border: 1px solid black; padding: 8px; text-align: left; }");
            out.println("th { background-color: #f2f2f2; }");
            out.println("</style></head><body>");
            out.println("<h1>Lista de Usuarios</h1>");
            out.println("<table><tr><th>ID</th><th>Nombre</th><th>Email</th><th>Fecha de Registro</th></tr>");

            // Mostrar usuarios en la tabla
            while (rs.next()) {
                out.println("<tr>");
                out.println("<td>" + rs.getInt("id") + "</td>");
                out.println("<td>" + rs.getString("nombre") + "</td>");
                out.println("<td>" + rs.getString("email") + "</td>");
                out.println("<td>" + rs.getTimestamp("fecha_registro") + "</td>");
                out.println("</tr>");
            }
            out.println("</table>");

            // Formulario para añadir nuevo usuario
            out.println("<h2>Añadir Nuevo Usuario</h2>");
            out.println("<form method='POST' action='addUser'>");
            out.println("Nombre: <input type='text' name='nombre' required><br>");
            out.println("Email: <input type='email' name='email' required><br>");
            out.println("Contraseña: <input type='password' name='contrasena' required><br>");
            out.println("<input type='submit' value='Añadir Usuario'>");
            out.println("</form>");

            out.println("</body></html>");

            // Clean up
            rs.close();
            stmt.close();
            conn.close();

        } catch (Exception e) {
            out.println("Error: " + e.getMessage());
        } finally {
            try {
                if (stmt != null) stmt.close();
                if (conn != null) conn.close();
            } catch (Exception e) {
                out.println("Error closing resources: " + e.getMessage());
            }
        }
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String nombre = request.getParameter("nombre");
        String email = request.getParameter("email");
        String contrasena = request.getParameter("contrasena");

        Connection conn = null;
        PreparedStatement pstmt = null;

        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            conn = DriverManager.getConnection(DB_URL, USER, PASS);

            String sql = "INSERT INTO usuarios (nombre, email, contrasena) VALUES (?, ?, ?)";
            pstmt = conn.prepareStatement(sql);
            pstmt.setString(1, nombre);
            pstmt.setString(2, email);
            pstmt.setString(3, contrasena);
            pstmt.executeUpdate();

            response.sendRedirect(request.getContextPath() + "/"); // Redirigir a doGet después de la inserción

        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            try {
                if (pstmt != null) pstmt.close();
                if (conn != null) conn.close();
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }
}
