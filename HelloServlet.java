// To save as "<TOMCAT_HOME>\webapps\hello\WEB-INF\classes\HelloServlet.java"
import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.annotation.*;
import org.python.util.PythonInterpreter; 
import org.python.core.*; 

@WebServlet("/sayhello")   // Configure the request URL for this servlet (Tomcat 7/Servlet 3.0 upwards)
public class HelloServlet extends HttpServlet {

   // The doGet() runs once per HTTP GET request to this servlet.
   @Override
   public void doGet(HttpServletRequest request, HttpServletResponse response)
         throws IOException, ServletException {
 
      // Set the response MIME type of the response message
      response.setContentType("text");
      // Allocate a output writer to write the response message into the network socket
      PrintWriter out = response.getWriter();

 
      InterpreterExample ie = new InterpreterExample();  

      ie.execfile("server.py");  

      PyInstance server = ie.createClass("Server"); 
      String params= request.getParameter("query");
      ie.interpreter.set("param", new PyString(params)); 
      PyObject obj = ie.interpreter.get("param");
      // out.println(obj);
      out.println(server.invoke("process_string", obj)); 
      // out.println(request.getParameter("query"));

      out.close();  // Always close the output writer
   }
}