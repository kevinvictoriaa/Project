# Project Kevin De La Victoria (200146034) and Omar Cifuentes(200152245) 
Codigo Uml en Python y requisito funcional.

@@startuml


class  Empleados{

-Nombre_empleado:str
-Apellidos_del_empleado:str
-Id_empleado:str
-Usuario:str
-Passaword:str


}


class Bartender extends  Empleados{

-barra: Barra

}
class Mesero extends  Empleados{

-mesas: Lis<Mesas>

}
class Hostess extends  Empleados
{

}
class Maitre extends  Empleados{

}


abstract class Cliente extends  Maitre {



}
abstract class Cliente extends  Hostess {

+Clietes: List<Cliente>

}



class Barra extends  Bartender{

+Clietes: List<Cliente>

}
 class Mesas  extends  Mesero {

-numeroMesa: int
-cantSillas: int
-clientes: List <Cliente>

}

 class Cocinero extends  Empleados {

#tipo 

}
 class Chef extends  Cocinero {


}
class Asistentes extends  Cocinero {


}

@@enduml

  
  
  
  
  
  
  
  

