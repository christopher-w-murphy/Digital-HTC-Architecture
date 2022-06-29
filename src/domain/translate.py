from deepl import Translate, DocumentTranslationException


def translate_document(input_path: str, output_path: str, auth_key: str) -> None
    tranlator = Translate(auth_key)
    try:
        translator.translate_document_from_filepath(
            input_path,
            output_path,
            source_lang='FR',
            target_lang='EN'
        )
    except DocumentTranslationException as error:
        doc_id = error.document_handle.id
        doc_key = error.document_handle.key
        print(f"Error after uploading ${error}, id: ${doc_id} key: ${doc_key}")
    except deepl.DeepLException as error:
        print(error)
