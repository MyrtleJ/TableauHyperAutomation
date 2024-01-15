import params
import tableauserverclient as TSC
import os
import pantab
import pandas as pd

def matching_list(df_1,df_2):
    return list(set(df_1) & set(df_2))

def difference_list(df_1,df_2):
    return list(set(df_2) - set(df_1))

def server_login(token_name=params.token_name, token_value=params.token_value,site_id=params.site_id,server_url=params.url):
    try:
        tableau_auth = TSC.PersonalAccessTokenAuth(token_name=token_name, personal_access_token=token_value, site_id=site_id)
        server = TSC.Server(server_address=server_url, use_server_version=True)
        server.auth.sign_in(tableau_auth)
    except:
        raise Exception("CUS-001: Server Login Error")

    return server

def server_logout(server):
    try:
        server.auth.sign_out()
        print("Logout Successful !!")
    except:
        raise Exception("CUS-002: Server logout failed")
    
def find_project_id(tableau_server,proj_name):

    request_options = TSC.RequestOptions(pagenumber=params.request_page, pagesize=params.request_pagesize)

    project_id = ''

    all_project_items, pagination_item = tableau_server.projects.get(req_options=request_options)
    all_project_items.sort(key=lambda x: x.name, reverse=False)
    
    for proj in all_project_items:
        if proj.name == proj_name:
            project_id = proj.id 
            break
    
    if project_id == '':
        raise Exception("CUS=003: Project name not available")
    else:
        return project_id
    
def load_data(tableau_server,folder_path=params.empty_string, file_name=params.empty_string, project_id=params.empty_string, encoding=params.encoding , pick_cols=params.empty_string , data_source_name = params.empty_string ):

    if folder_path != '' :
        load_full_folder(tableau_server,folder_path,project_id,encoding,pick_cols,data_source_name)
    elif file_name != '' :
        load_single_file(tableau_server,file_name,project_id,encoding,pick_cols,data_source_name)

def load_full_folder(tableau_server,folder_path,project_id,encoding=params.encoding , pick_cols=params.empty_string, data_source_name = params.empty_string):
    count_files = 0
    error_File_cnt = 0
    overwrite_files = True
    for x in os.listdir(folder_path):
        file_path = folder_path + "/"+x
        file_name, file_extension = os.path.splitext( os.path.basename(file_path))

        if file_extension == '.csv':
            df = pd.read_csv(file_path,encoding=encoding)
        elif file_extension == '.xls' or file_extension == '.xlsx':
            df = pd.read_excel(file_path,encoding=encoding)
        else:
            continue
        
        if pick_cols != '':
            col_headers = df.columns.values.tolist()
            matched_col = matching_list(  col_headers , pick_cols )
            diff_col = difference_list(col_headers, pick_cols)

            df = df[matched_col]
            df = df.reindex(columns=[*df.columns.values.tolist(), *diff_col], fill_value="")

        if data_source_name != '':
            file_name = data_source_name
            

        pantab.frame_to_hyper(df, file_name+".hyper", table=file_name)
        h_file_path = './'+file_name+'.hyper'

        try:
            new_datasource = TSC.DatasourceItem(project_id)
            if overwrite_files == True:
                new_datasource = tableau_server.datasources.publish(new_datasource, h_file_path, 'Overwrite')
                if data_source_name != '': overwrite_files = False
            elif overwrite_files == False:
                new_datasource = tableau_server.datasources.publish(new_datasource, h_file_path, 'Append')
            
            count_files = count_files + 1
            print(count_files , ' - Completed : ' , file_path)
        except:
            error_File_cnt = error_File_cnt+1
            print(error_File_cnt , " ***** Error File in updating **** " , file_path)

        finally:
            # remove the local Hyper File
            if os.path.exists(h_file_path):
                os.remove(h_file_path)
                print("     Local Hyper File Removed.")
            else:
                print("The file does not exist")

    print('************ Summary **********')
    print('Total Files Processed : ',count_files)
    print('Error Files :',error_File_cnt)

def load_single_file(tableau_server,file_name,project_id,encoding=params.encoding, pick_cols=params.empty_string , data_source_name=params.empty_string):

    lfile_name, lfile_extension = os.path.splitext( os.path.basename(file_name))

    if lfile_extension == '.csv':
        df = pd.read_csv(file_name,encoding=encoding)
    elif lfile_extension == '.xls' or lfile_extension == '.xlsx':
        df = pd.read_excel(file_name,encoding=encoding)

    if pick_cols != '':
        col_headers = df.columns.values.tolist()
        matched_col = matching_list(  col_headers , pick_cols )
        diff_col = difference_list(col_headers, pick_cols)

        df = df[matched_col]
        df = df.reindex(columns=[*df.columns.values.tolist(), *diff_col], fill_value="")

    if data_source_name != '':
        file_name = data_source_name

    pantab.frame_to_hyper(df, lfile_name+".hyper", table=lfile_name)
    hfile_path = './'+lfile_name+'.hyper'

    new_datasource = TSC.DatasourceItem(project_id)
    new_datasource = tableau_server.datasources.publish(new_datasource, hfile_path, 'Overwrite')
    
