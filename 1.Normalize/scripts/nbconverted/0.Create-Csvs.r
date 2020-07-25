library(tidyverse)

get_db <- function(filepath){

    db <- DBI::dbConnect(RSQLite::SQLite(), filepath)
    return(db)
}

## 1. Establish a connection to the database file
## 2. Load all 4 tables
## 3. Merge the metadata (Image) table with the other three
## 4. Print csvs that will be easy to use.

main_function <- function(filepath, platemappath){

    metadata <- readr::read_csv(platemappath)

    sc_db = get_db(filepath)

    imagedata <- tbl(src = sc_db, "image")
    cells <- tbl(src = sc_db, "cells")
    cytoplasm <- tbl(src = sc_db, "cytoplasm")
    nuclei <- tbl(src = sc_db, "nuclei")

    platemetadata = imagedata %>% select(contains("Metadata") | contains("TableNumber")) %>% select(-c(Metadata_Series, Metadata_Site, Metadata_ChannelNumber, Metadata_FileLocation, Metadata_Frame, ExecutionTime_02Metadata, ModuleError_02Metadata))

    cells_meta = left_join(platemetadata, cells)
    nuc_meta = left_join(platemetadata, nuclei)
    cyto_meta = left_join(platemetadata, cytoplasm)

    write_csv(as.data.frame(cyto_meta), "Unnormalized_Batch2_Cytoplasm.csv")
    write_csv(as.data.frame(nuc_meta), "Unnormalized_Batch2_Nuclei.csv")
    write_csv(as.data.frame(cells_meta), "Unnormalized_Batch2_Cells.csv")
    
}


main_function("/home/ubuntu/bucket/projects/2018_05_30_ResistanceMechanisms_Kapoor/workspace/backend/2019_03_20_Batch2/207106_exposure320/207106_exposure320.sqlite", "/home/ubuntu/bucket/projects/2018_05_30_ResistanceMechanisms_Kapoor/workspace/metadata/2019_03_20_Batch2/barcode_platemap.csv")






