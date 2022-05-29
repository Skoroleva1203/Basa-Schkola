import ui
import add_data
import log

def run():
    a = ui.find()
    if a == 1:
        list_nm, list_cl, list_adr = add_data.add_anketa()
        log.write_file_name(list_nm)
        log.write_file_class(list_cl)
        log.write_file_adress(list_adr)
        run()

    if a == 2:
        return