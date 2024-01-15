import TableauDataLoadUtils as TUtils
import params
project_name1 = "Project Name"
load_full_folder = '\\\\FolderLocation'
load_file = ''
local_encoding = 'UTF-16'
local_ds_name = 'DatasourceName'

def main():

        server = TUtils.server_login()
        project_id1 = TUtils.find_project_id(proj_name=project_name1,tableau_server=server)

        # Load specific file:
        #TUtils.load_data(tableau_server=server,project_id=project_id1,file_name=load_file)

        # Load all files in folder:
        #TUtils.load_data(tableau_server=server,project_id=project_id1,folder_path=load_full_folder)

        # Load all files in folder with specific columns with encoding
        TUtils.load_data(tableau_server=server,project_id=project_id1,folder_path=load_full_folder,pick_cols=params.base_lims_loc_col,encoding=local_encoding,data_source_name=local_ds_name)


        TUtils.server_logout(server=server)

if __name__=='__main__':
    main()
