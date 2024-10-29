package com.ejemplo;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import javax.xml.parsers.DocumentBuilderFactory;
import org.w3c.dom.Document;
import org.w3c.dom.Element;

public class App {

    public static void main(String[] args) {
        try {
            // Cargar la configuración desde config.xml
            Document config = DocumentBuilderFactory.newInstance().newDocumentBuilder().parse("config.xml");
            config.getDocumentElement().normalize();
            Element dbElement = (Element) config.getElementsByTagName("database").item(0);

            String url = dbElement.getElementsByTagName("url").item(0).getTextContent();
            String user = dbElement.getElementsByTagName("username").item(0).getTextContent();
            String password = dbElement.getElementsByTagName("password").item(0).getTextContent();

            // Intenta conectar con la base de datos
            Connection connection = DriverManager.getConnection(url, user, password);
            System.out.println("Conexión a la base de datos establecida exitosamente.");

            connection.close();
            System.out.println("Conexión cerrada.");
        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
