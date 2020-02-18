// package interpret;

import org.python.util.PythonInterpreter; 
import org.python.core.*; 

public class InterpreterExample  
{  

   public PythonInterpreter interpreter = null;  


   public InterpreterExample()  
   {  
      interpreter= new PythonInterpreter();
      PythonInterpreter.initialize(System.getProperties(),  
                                   System.getProperties(), new String[0]);  

      this.interpreter = new PythonInterpreter();  
   }  

   void execfile( final String fileName )  
   {  
      this.interpreter.execfile(fileName);  
   }  

   PyInstance createClass( final String className)  
   {  
      return (PyInstance) this.interpreter.eval(className + "()");  
   }  

}