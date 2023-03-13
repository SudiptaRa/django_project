from rest_framework.response import Response
from allocation_engine.models import Employee_table
from allocation_engine.serializers import employeeSerializer
from rest_framework import status






class Controller:
    def create_employee_details(self,request):
        try:
            new_data={}
            if request.data:
                new_data['id'] = request.data['id']
                new_data['empid'] = request.data['empid']
                if request.data['empname']:
                    new_data['empname'] = request.data['empname']
                else:
                    return {"error": True, "message": "employee name is empty", "status": 400}
                if request.data['empemail']:
                    new_data['empemail'] = request.data['empemail']
                else:
                    return {"error": True, "message": "employee email is empty", "status": 400}
                if request.data['emppassword']:
                    new_data['emppassword'] = request.data['emppassword'] 
                else:
                    return {"error": True, "message": "employee password is empty", "status": 400}
                if request.data['empexp']:  
                    new_data['empexp'] = request.data['empexp'] 
                else:
                    return {"error": True, "message": "employee exp is empty", "status": 400}    
                employee_data = employeeSerializer(data=new_data)
                if employee_data.is_valid():
                    obj = employee_data.save()
                    return {"message": "success", "status": 200}
            else:
                return {"error": True, "message": "please provide details", "status": 400}
        except:
                return {"error": True, "message": "Exception please provide details", "status": 400}




    def update_employee_details(self,request):
        try:
            new_data={}
            if request.data:
                if 'empid' in request.data and request.data['empid']:
                    new_data['empid'] = request.data['empid']
                if 'empname' in request.data:
                    new_data['empname'] = request.data['empname']
                if 'empemail' in request.data:
                    new_data['empemail'] = request.data['empemail']
                if 'emppassword' in request.data:
                    new_data['emppassword'] = request.data['emppassword'] 
                if 'empexp' in request.data:  
                    new_data['empexp'] = request.data['empexp'] 
                return (new_data)
            else:
                return {"error": True, "message": "please provide details", "status": 400}
        except Exception as ex:
            return {"error": True, "message": f"Exception please provide details {ex}", "status": 400}






        #     def update(self,request):
        # update_res={}
        # if 'id' not in request.data:
        #     return Response({"error": False, "message": "please provide id to update records", "status": 400}, status=status.HTTP_400_BAD_REQUEST)

        # employee_data_set = Employee_table.objects.filter(id = request.data['id']).values()
        # # print()
        # updt_obj = controller.Controller()
        # update_res = updt_obj.update_employee_details(request,employee_data_set)
        # if 'error' not in update_res:
        #     return Response({"error": False, "message": "success", "status": 200}, status=status.HTTP_200_OK)
        # else:
        #     return Response({"error": False, "message": "failed", "status": 400}, status=status.HTTP_400_BAD_REQUEST)

