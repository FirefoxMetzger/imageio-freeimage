from pathlib import Path


class FreeImage:
    macros = [
        ("WIN32", None),
        ("NDEBUG", None),
        ("_WINDOWS", None),
        ("_USRDLL", None),
        ("OPJ_STATIC", None),
        ("FREEIMAGE_EXPORTS", None),
        ("_CRT_SECURE_NO_DEPRECATE", None),
        ("LIBRAW_NODLL", None),
    ]
    source = [
        *[str(x) for x in Path("FreeImage/Source/FreeImage").glob("*.cpp")],
        *[str(x) for x in Path("FreeImage/Source/Metadata").glob("*.cpp")],
        *[str(x) for x in Path("FreeImage/Source/FreeImageToolkit").glob("*.cpp")],
        *[str(x) for x in Path("FreeImage/Source/FreeImage").glob("*.c")],
        *[str(x) for x in Path("FreeImage/Source/Metadata").glob("*.c")],
        *[str(x) for x in Path("FreeImage/Source/FreeImageToolkit").glob("*.c")],
    ]
    include = [
        "FreeImage/Source",
        "FreeImage/Source/ZLib",
        "FreeImage/Source/DeprecationManager",
        "FreeImage/Source/OpenEXR",
        "FreeImage/Source/OpenEXR/Half",
        "FreeImage/Source/OpenEXR/Iex",
        "FreeImage/Source/OpenEXR/IlmImf",
        "FreeImage/Source/OpenEXR/Imath",
        "FreeImage/Source/OpenEXR/IlmThread",
        "FreeImage/Source/LibJXR/jxrgluelib",
        "FreeImage/Source/LibJXR/image/sys",
    ]
    libraries = [
        "jpeg",
        "jxr",
        "openjpeg",
        "png",
        "rawlite",
        "tiff4",
        "webp",
        "openexr",
        "zlib",
    ]


class LibJPEG:
    macros = [
        ("WIN32", None),
        ("NDEBUG", None),
        ("_LIB", None),
        ("_CRT_SECURE_NO_DEPRECATE", None),
    ]
    source = [
        "FreeImage/Source/LibJPEG/jaricom.c",
        "FreeImage/Source/LibJPEG/jcapimin.c",
        "FreeImage/Source/LibJPEG/jcapistd.c",
        "FreeImage/Source/LibJPEG/jcarith.c",
        "FreeImage/Source/LibJPEG/jccoefct.c",
        "FreeImage/Source/LibJPEG/jccolor.c",
        "FreeImage/Source/LibJPEG/jcdctmgr.c",
        "FreeImage/Source/LibJPEG/jchuff.c",
        "FreeImage/Source/LibJPEG/jcinit.c",
        "FreeImage/Source/LibJPEG/jcmainct.c",
        "FreeImage/Source/LibJPEG/jcmarker.c",
        "FreeImage/Source/LibJPEG/jcmaster.c",
        "FreeImage/Source/LibJPEG/jcomapi.c",
        "FreeImage/Source/LibJPEG/jcparam.c",
        "FreeImage/Source/LibJPEG/jcprepct.c",
        "FreeImage/Source/LibJPEG/jcsample.c",
        "FreeImage/Source/LibJPEG/jctrans.c",
        "FreeImage/Source/LibJPEG/jdapimin.c",
        "FreeImage/Source/LibJPEG/jdapistd.c",
        "FreeImage/Source/LibJPEG/jdarith.c",
        "FreeImage/Source/LibJPEG/jdatadst.c",
        "FreeImage/Source/LibJPEG/jdatasrc.c",
        "FreeImage/Source/LibJPEG/jdcoefct.c",
        "FreeImage/Source/LibJPEG/jdcolor.c",
        "FreeImage/Source/LibJPEG/jddctmgr.c",
        "FreeImage/Source/LibJPEG/jdhuff.c",
        "FreeImage/Source/LibJPEG/jdinput.c",
        "FreeImage/Source/LibJPEG/jdmainct.c",
        "FreeImage/Source/LibJPEG/jdmarker.c",
        "FreeImage/Source/LibJPEG/jdmaster.c",
        "FreeImage/Source/LibJPEG/jdmerge.c",
        "FreeImage/Source/LibJPEG/jdpostct.c",
        "FreeImage/Source/LibJPEG/jdsample.c",
        "FreeImage/Source/LibJPEG/jdtrans.c",
        "FreeImage/Source/LibJPEG/jerror.c",
        "FreeImage/Source/LibJPEG/jfdctflt.c",
        "FreeImage/Source/LibJPEG/jfdctfst.c",
        "FreeImage/Source/LibJPEG/jfdctint.c",
        "FreeImage/Source/LibJPEG/jidctflt.c",
        "FreeImage/Source/LibJPEG/jidctfst.c",
        "FreeImage/Source/LibJPEG/jidctint.c",
        "FreeImage/Source/LibJPEG/jmemmgr.c",
        "FreeImage/Source/LibJPEG/jmemnobs.c",
        "FreeImage/Source/LibJPEG/jquant1.c",
        "FreeImage/Source/LibJPEG/jquant2.c",
        "FreeImage/Source/LibJPEG/jutils.c",
        "FreeImage/Source/LibJPEG/transupp.c",
    ]
    include = [
        "FreeImage/Source/ZLib",
    ]


class LibJXR:
    macros = [
        ("WIN32", None),
        ("NDEBUG", None),
        ("_LIB", None),
        ("DISABLE_PERF_MEASUREMENT", None),
    ]

    source = [
        "FreeImage/Source/LibJXR/image/decode/decode.c",
        "FreeImage/Source/LibJXR/image/decode/JXRTranscode.c",
        "FreeImage/Source/LibJXR/image/decode/postprocess.c",
        "FreeImage/Source/LibJXR/image/decode/segdec.c",
        "FreeImage/Source/LibJXR/image/decode/strdec.c",
        "FreeImage/Source/LibJXR/image/decode/strdec_x86.c",
        "FreeImage/Source/LibJXR/image/decode/strInvTransform.c",
        "FreeImage/Source/LibJXR/image/decode/strPredQuantDec.c",
        "FreeImage/Source/LibJXR/image/encode/encode.c",
        "FreeImage/Source/LibJXR/image/encode/segenc.c",
        "FreeImage/Source/LibJXR/image/encode/strenc.c",
        "FreeImage/Source/LibJXR/image/encode/strenc_x86.c",
        "FreeImage/Source/LibJXR/image/encode/strFwdTransform.c",
        "FreeImage/Source/LibJXR/image/encode/strPredQuantEnc.c",
        "FreeImage/Source/LibJXR/image/sys/adapthuff.c",
        "FreeImage/Source/LibJXR/image/sys/image.c",
        "FreeImage/Source/LibJXR/image/sys/strcodec.c",
        "FreeImage/Source/LibJXR/image/sys/strPredQuant.c",
        "FreeImage/Source/LibJXR/image/sys/strTransform.c",
        "FreeImage/Source/LibJXR/jxrgluelib/JXRGlue.c",
        "FreeImage/Source/LibJXR/jxrgluelib/JXRGlueJxr.c",
        "FreeImage/Source/LibJXR/jxrgluelib/JXRGluePFC.c",
        "FreeImage/Source/LibJXR/jxrgluelib/JXRMeta.c",
    ]

    include = [
        "FreeImage/Source/LibJXR/image/sys",
        "FreeImage/Source/LibJXR/jxrgluelib",
    ]


class LibOpenJPEG:
    macros = [
        ("WIN32", None),
        ("NDEBUG", None),
        ("_LIB", None),
        ("OPJ_STATIC", None),
        ("_CRT_SECURE_NO_DEPRECATE", None),
    ]
    source = [
        "FreeImage/Source/LibOpenJPEG/bio.c",
        "FreeImage/Source/LibOpenJPEG/cio.c",
        "FreeImage/Source/LibOpenJPEG/dwt.c",
        "FreeImage/Source/LibOpenJPEG/event.c",
        "FreeImage/Source/LibOpenJPEG/function_list.c",
        "FreeImage/Source/LibOpenJPEG/image.c",
        "FreeImage/Source/LibOpenJPEG/invert.c",
        "FreeImage/Source/LibOpenJPEG/j2k.c",
        "FreeImage/Source/LibOpenJPEG/jp2.c",
        "FreeImage/Source/LibOpenJPEG/mct.c",
        "FreeImage/Source/LibOpenJPEG/mqc.c",
        "FreeImage/Source/LibOpenJPEG/openjpeg.c",
        "FreeImage/Source/LibOpenJPEG/opj_clock.c",
        "FreeImage/Source/LibOpenJPEG/pi.c",
        "FreeImage/Source/LibOpenJPEG/raw.c",
        "FreeImage/Source/LibOpenJPEG/t1.c",
        "FreeImage/Source/LibOpenJPEG/t2.c",
        "FreeImage/Source/LibOpenJPEG/tcd.c",
        "FreeImage/Source/LibOpenJPEG/tgt.c",
    ]
    include = []


class LibPNG:
    macros = [
        ("WIN32", None),
        ("NDEBUG", None),
        ("_LIB", None),
        ("_CRT_SECURE_NO_DEPRECATE", None),
    ]
    source = [
        "FreeImage/Source/LibPNG/png.c",
        "FreeImage/Source/LibPNG/pngerror.c",
        "FreeImage/Source/LibPNG/pngget.c",
        "FreeImage/Source/LibPNG/pngmem.c",
        "FreeImage/Source/LibPNG/pngpread.c",
        "FreeImage/Source/LibPNG/pngread.c",
        "FreeImage/Source/LibPNG/pngrio.c",
        "FreeImage/Source/LibPNG/pngrtran.c",
        "FreeImage/Source/LibPNG/pngrutil.c",
        "FreeImage/Source/LibPNG/pngset.c",
        "FreeImage/Source/LibPNG/pngtrans.c",
        "FreeImage/Source/LibPNG/pngwio.c",
        "FreeImage/Source/LibPNG/pngwrite.c",
        "FreeImage/Source/LibPNG/pngwtran.c",
        "FreeImage/Source/LibPNG/pngwutil.c",
    ]
    include = [
        "FreeImage/Source/ZLib",
    ]


class LibRawLite:
    macros = [
        ("WIN32", None),
        ("NDEBUG", None),
        ("_LIB", None),
        ("_CRT_SECURE_NO_WARNINGS", None),
        ("LIBRAW_NODLL", None),
    ]
    source = [
        "FreeImage/Source/LibRawLite/internal/dcraw_common.cpp",
        "FreeImage/Source/LibRawLite/internal/dcraw_fileio.cpp",
        "FreeImage/Source/LibRawLite/internal/demosaic_packs.cpp",
        "FreeImage/Source/LibRawLite/src/libraw_c_api.cpp",
        "FreeImage/Source/LibRawLite/src/libraw_cxx.cpp",
        "FreeImage/Source/LibRawLite/src/libraw_datastream.cpp",
    ]
    include = [
        "FreeImage/Source/LibRawLite",
        "FreeImage/Source/ZLib",
    ]


class LibTIFF4:
    macros = [
        ("WIN32", None),
        ("NDEBUG", None),
        ("_LIB", None),
        ("_CRT_SECURE_NO_DEPRECATE", None),
    ]
    source = [
        "FreeImage/Source/LibTIFF4/tif_aux.c",
        "FreeImage/Source/LibTIFF4/tif_close.c",
        "FreeImage/Source/LibTIFF4/tif_codec.c",
        "FreeImage/Source/LibTIFF4/tif_color.c",
        "FreeImage/Source/LibTIFF4/tif_compress.c",
        "FreeImage/Source/LibTIFF4/tif_dir.c",
        "FreeImage/Source/LibTIFF4/tif_dirinfo.c",
        "FreeImage/Source/LibTIFF4/tif_dirread.c",
        "FreeImage/Source/LibTIFF4/tif_dirwrite.c",
        "FreeImage/Source/LibTIFF4/tif_dumpmode.c",
        "FreeImage/Source/LibTIFF4/tif_error.c",
        "FreeImage/Source/LibTIFF4/tif_extension.c",
        "FreeImage/Source/LibTIFF4/tif_fax3.c",
        "FreeImage/Source/LibTIFF4/tif_fax3sm.c",
        "FreeImage/Source/LibTIFF4/tif_flush.c",
        "FreeImage/Source/LibTIFF4/tif_getimage.c",
        "FreeImage/Source/LibTIFF4/tif_jpeg.c",
        "FreeImage/Source/LibTIFF4/tif_luv.c",
        "FreeImage/Source/LibTIFF4/tif_lzma.c",
        "FreeImage/Source/LibTIFF4/tif_lzw.c",
        "FreeImage/Source/LibTIFF4/tif_next.c",
        "FreeImage/Source/LibTIFF4/tif_ojpeg.c",
        "FreeImage/Source/LibTIFF4/tif_open.c",
        "FreeImage/Source/LibTIFF4/tif_packbits.c",
        "FreeImage/Source/LibTIFF4/tif_pixarlog.c",
        "FreeImage/Source/LibTIFF4/tif_predict.c",
        "FreeImage/Source/LibTIFF4/tif_print.c",
        "FreeImage/Source/LibTIFF4/tif_read.c",
        "FreeImage/Source/LibTIFF4/tif_strip.c",
        "FreeImage/Source/LibTIFF4/tif_swab.c",
        "FreeImage/Source/LibTIFF4/tif_thunder.c",
        "FreeImage/Source/LibTIFF4/tif_tile.c",
        "FreeImage/Source/LibTIFF4/tif_version.c",
        "FreeImage/Source/LibTIFF4/tif_warning.c",
        "FreeImage/Source/LibTIFF4/tif_write.c",
        "FreeImage/Source/LibTIFF4/tif_zip.c",
    ]
    include = [
        "FreeImage/Source/ZLib",
        "FreeImage/Source/LibJPEG",
    ]


class LibWebP:
    macros = [
        ("WIN32", None),
        ("NDEBUG", None),
        ("_LIB", None),
    ]
    source = [str(x) for x in Path("FreeImage/Source/LibWebP/src/").glob("**/*.c")]
    include = ["FreeImage/Source/LibWebP"]


class OpenEXR:
    macros = [
        ("WIN32", None),
        ("NDEBUG", None),
        ("_LIB", None),
        ("_CRT_SECURE_NO_DEPRECATE", None),
    ]
    source = [
        "FreeImage/Source/OpenEXR/IexMath/IexMathFpu.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/b44ExpLogTable.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfAcesFile.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfAttribute.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfB44Compressor.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfBoxAttribute.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfChannelList.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfChannelListAttribute.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfChromaticities.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfChromaticitiesAttribute.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfCompositeDeepScanLine.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfCompressionAttribute.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfCompressor.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfConvert.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfCRgbaFile.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfDeepCompositing.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfDeepFrameBuffer.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfDeepImageStateAttribute.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfDeepScanLineInputFile.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfDeepScanLineInputPart.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfDeepScanLineOutputFile.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfDeepScanLineOutputPart.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfDeepTiledInputFile.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfDeepTiledInputPart.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfDeepTiledOutputFile.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfDeepTiledOutputPart.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfDoubleAttribute.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfDwaCompressor.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfEnvmap.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfEnvmapAttribute.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfFastHuf.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfFloatAttribute.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfFloatVectorAttribute.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfFrameBuffer.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfFramesPerSecond.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfGenericInputFile.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfGenericOutputFile.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfHeader.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfHuf.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfInputFile.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfInputPart.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfInputPartData.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfIntAttribute.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfIO.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfKeyCode.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfKeyCodeAttribute.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfLineOrderAttribute.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfLut.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfMatrixAttribute.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfMisc.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfMultiPartInputFile.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfMultiPartOutputFile.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfMultiView.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfOpaqueAttribute.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfOutputFile.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfOutputPart.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfOutputPartData.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfPartType.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfPizCompressor.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfPreviewImage.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfPreviewImageAttribute.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfPxr24Compressor.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfRational.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfRationalAttribute.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfRgbaFile.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfRgbaYca.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfRle.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfRleCompressor.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfScanLineInputFile.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfStandardAttributes.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfStdIO.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfStringAttribute.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfStringVectorAttribute.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfSystemSpecific.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfTestFile.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfThreading.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfTileDescriptionAttribute.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfTiledInputFile.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfTiledInputPart.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfTiledMisc.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfTiledOutputFile.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfTiledOutputPart.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfTiledRgbaFile.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfTileOffsets.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfTimeCode.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfTimeCodeAttribute.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfVecAttribute.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfVersion.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfWav.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfZip.cpp",
        "FreeImage/Source/OpenEXR/IlmImf/ImfZipCompressor.cpp",
        "FreeImage/Source/OpenEXR/Imath/ImathBox.cpp",
        "FreeImage/Source/OpenEXR/Imath/ImathColorAlgo.cpp",
        "FreeImage/Source/OpenEXR/Imath/ImathFun.cpp",
        "FreeImage/Source/OpenEXR/Imath/ImathMatrixAlgo.cpp",
        "FreeImage/Source/OpenEXR/Imath/ImathRandom.cpp",
        "FreeImage/Source/OpenEXR/Imath/ImathShear.cpp",
        "FreeImage/Source/OpenEXR/Imath/ImathVec.cpp",
        "FreeImage/Source/OpenEXR/Iex/IexBaseExc.cpp",
        "FreeImage/Source/OpenEXR/Iex/IexThrowErrnoExc.cpp",
        "FreeImage/Source/OpenEXR/Half/half.cpp",
        "FreeImage/Source/OpenEXR/IlmThread/IlmThread.cpp",
        "FreeImage/Source/OpenEXR/IlmThread/IlmThreadMutex.cpp",
        "FreeImage/Source/OpenEXR/IlmThread/IlmThreadPool.cpp",
        "FreeImage/Source/OpenEXR/IlmThread/IlmThreadSemaphore.cpp",
        "FreeImage/Source/OpenEXR/IexMath/IexMathFloatExc.cpp",
    ]
    include = [
        "FreeImage/Source/OpenEXR/",
        "FreeImage/Source/OpenEXR/IlmImf",
        "FreeImage/Source/OpenEXR/Imath",
        "FreeImage/Source/OpenEXR/IexMath",
        "FreeImage/Source/OpenEXR/Iex",
        "FreeImage/Source/OpenEXR/Half",
        "FreeImage/Source/OpenEXR/IlmThread",
        "FreeImage/Source/ZLib",
    ]
    libraries = ["zlib"]


class ZLib:
    macros = [
        ("WIN32", None),
        ("NDEBUG", None),
        ("_LIB", None),
        ("_CRT_SECURE_NO_DEPRECATE", None),
        ("_CRT_SECURE_NO_WARNINGS", None),
        ("_SCL_SECURE_NO_WARNINGS", None),
    ]
    source = [str(x) for x in Path("FreeImage/Source/Zlib").glob("*.c")]
    include = []
