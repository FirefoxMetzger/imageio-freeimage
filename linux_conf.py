freeimage = {
    "shared": True,
    "sources": [
        "FreeImage/Source/FreeImage/BitmapAccess.cpp",
        "FreeImage/Source/FreeImage/ColorLookup.cpp",
        "FreeImage/Source/FreeImage/ConversionRGBA16.cpp",
        "FreeImage/Source/FreeImage/ConversionRGBAF.cpp",
        "FreeImage/Source/FreeImage/FreeImage.cpp",
        "FreeImage/Source/FreeImage/FreeImageC.c",
        "FreeImage/Source/FreeImage/FreeImageIO.cpp",
        "FreeImage/Source/FreeImage/GetType.cpp",
        "FreeImage/Source/FreeImage/LFPQuantizer.cpp",
        "FreeImage/Source/FreeImage/MemoryIO.cpp",
        "FreeImage/Source/FreeImage/PixelAccess.cpp",
        "FreeImage/Source/FreeImage/J2KHelper.cpp",
        "FreeImage/Source/FreeImage/MNGHelper.cpp",
        "FreeImage/Source/FreeImage/Plugin.cpp",
        "FreeImage/Source/FreeImage/PluginBMP.cpp",
        "FreeImage/Source/FreeImage/PluginCUT.cpp",
        "FreeImage/Source/FreeImage/PluginDDS.cpp",
        "FreeImage/Source/FreeImage/PluginEXR.cpp",
        "FreeImage/Source/FreeImage/PluginG3.cpp",
        "FreeImage/Source/FreeImage/PluginGIF.cpp",
        "FreeImage/Source/FreeImage/PluginHDR.cpp",
        "FreeImage/Source/FreeImage/PluginICO.cpp",
        "FreeImage/Source/FreeImage/PluginIFF.cpp",
        "FreeImage/Source/FreeImage/PluginJ2K.cpp",
        "FreeImage/Source/FreeImage/PluginJNG.cpp",
        "FreeImage/Source/FreeImage/PluginJP2.cpp",
        "FreeImage/Source/FreeImage/PluginJPEG.cpp",
        "FreeImage/Source/FreeImage/PluginJXR.cpp",
        "FreeImage/Source/FreeImage/PluginKOALA.cpp",
        "FreeImage/Source/FreeImage/PluginMNG.cpp",
        "FreeImage/Source/FreeImage/PluginPCD.cpp",
        "FreeImage/Source/FreeImage/PluginPCX.cpp",
        "FreeImage/Source/FreeImage/PluginPFM.cpp",
        "FreeImage/Source/FreeImage/PluginPICT.cpp",
        "FreeImage/Source/FreeImage/PluginPNG.cpp",
        "FreeImage/Source/FreeImage/PluginPNM.cpp",
        "FreeImage/Source/FreeImage/PluginPSD.cpp",
        "FreeImage/Source/FreeImage/PluginRAS.cpp",
        "FreeImage/Source/FreeImage/PluginRAW.cpp",
        "FreeImage/Source/FreeImage/PluginSGI.cpp",
        "FreeImage/Source/FreeImage/PluginTARGA.cpp",
        "FreeImage/Source/FreeImage/PluginTIFF.cpp",
        "FreeImage/Source/FreeImage/PluginWBMP.cpp",
        "FreeImage/Source/FreeImage/PluginWebP.cpp",
        "FreeImage/Source/FreeImage/PluginXBM.cpp",
        "FreeImage/Source/FreeImage/PluginXPM.cpp",
        "FreeImage/Source/FreeImage/PSDParser.cpp",
        "FreeImage/Source/FreeImage/TIFFLogLuv.cpp",
        "FreeImage/Source/FreeImage/Conversion.cpp",
        "FreeImage/Source/FreeImage/Conversion16_555.cpp",
        "FreeImage/Source/FreeImage/Conversion16_565.cpp",
        "FreeImage/Source/FreeImage/Conversion24.cpp",
        "FreeImage/Source/FreeImage/Conversion32.cpp",
        "FreeImage/Source/FreeImage/Conversion4.cpp",
        "FreeImage/Source/FreeImage/Conversion8.cpp",
        "FreeImage/Source/FreeImage/ConversionFloat.cpp",
        "FreeImage/Source/FreeImage/ConversionRGB16.cpp",
        "FreeImage/Source/FreeImage/ConversionRGBF.cpp",
        "FreeImage/Source/FreeImage/ConversionType.cpp",
        "FreeImage/Source/FreeImage/ConversionUINT16.cpp",
        "FreeImage/Source/FreeImage/Halftoning.cpp",
        "FreeImage/Source/FreeImage/tmoColorConvert.cpp",
        "FreeImage/Source/FreeImage/tmoDrago03.cpp",
        "FreeImage/Source/FreeImage/tmoFattal02.cpp",
        "FreeImage/Source/FreeImage/tmoReinhard05.cpp",
        "FreeImage/Source/FreeImage/ToneMapping.cpp",
        "FreeImage/Source/FreeImage/NNQuantizer.cpp",
        "FreeImage/Source/FreeImage/WuQuantizer.cpp",
        "FreeImage/Source/FreeImage/CacheFile.cpp",
        "FreeImage/Source/FreeImage/MultiPage.cpp",
        "FreeImage/Source/FreeImage/ZLibInterface.cpp",
        "FreeImage/Source/Metadata/Exif.cpp",
        "FreeImage/Source/Metadata/FIRational.cpp",
        "FreeImage/Source/Metadata/FreeImageTag.cpp",
        "FreeImage/Source/Metadata/IPTC.cpp",
        "FreeImage/Source/Metadata/TagConversion.cpp",
        "FreeImage/Source/Metadata/TagLib.cpp",
        "FreeImage/Source/Metadata/XTIFF.cpp",
        "FreeImage/Source/FreeImageToolkit/Background.cpp",
        "FreeImage/Source/FreeImageToolkit/BSplineRotate.cpp",
        "FreeImage/Source/FreeImageToolkit/Channels.cpp",
        "FreeImage/Source/FreeImageToolkit/ClassicRotate.cpp",
        "FreeImage/Source/FreeImageToolkit/Colors.cpp",
        "FreeImage/Source/FreeImageToolkit/CopyPaste.cpp",
        "FreeImage/Source/FreeImageToolkit/Display.cpp",
        "FreeImage/Source/FreeImageToolkit/Flip.cpp",
        "FreeImage/Source/FreeImageToolkit/JPEGTransform.cpp",
        "FreeImage/Source/FreeImageToolkit/MultigridPoissonSolver.cpp",
        "FreeImage/Source/FreeImageToolkit/Rescale.cpp",
        "FreeImage/Source/FreeImageToolkit/Resize.cpp",
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
        "FreeImage/Source/ZLib/adler32.c",
        "FreeImage/Source/ZLib/compress.c",
        "FreeImage/Source/ZLib/crc32.c",
        "FreeImage/Source/ZLib/deflate.c",
        "FreeImage/Source/ZLib/gzclose.c",
        "FreeImage/Source/ZLib/gzlib.c",
        "FreeImage/Source/ZLib/gzread.c",
        "FreeImage/Source/ZLib/gzwrite.c",
        "FreeImage/Source/ZLib/infback.c",
        "FreeImage/Source/ZLib/inffast.c",
        "FreeImage/Source/ZLib/inflate.c",
        "FreeImage/Source/ZLib/inftrees.c",
        "FreeImage/Source/ZLib/trees.c",
        "FreeImage/Source/ZLib/uncompr.c",
        "FreeImage/Source/ZLib/zutil.c",
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
        "FreeImage/Source/LibRawLite/internal/dcraw_common.cpp",
        "FreeImage/Source/LibRawLite/internal/dcraw_fileio.cpp",
        "FreeImage/Source/LibRawLite/internal/demosaic_packs.cpp",
        "FreeImage/Source/LibRawLite/src/libraw_c_api.cpp",
        "FreeImage/Source/LibRawLite/src/libraw_cxx.cpp",
        "FreeImage/Source/LibRawLite/src/libraw_datastream.cpp",
        "FreeImage/Source/LibWebP/src/dec/alpha_dec.c",
        "FreeImage/Source/LibWebP/src/dec/buffer_dec.c",
        "FreeImage/Source/LibWebP/src/dec/frame_dec.c",
        "FreeImage/Source/LibWebP/src/dec/idec_dec.c",
        "FreeImage/Source/LibWebP/src/dec/io_dec.c",
        "FreeImage/Source/LibWebP/src/dec/quant_dec.c",
        "FreeImage/Source/LibWebP/src/dec/tree_dec.c",
        "FreeImage/Source/LibWebP/src/dec/vp8l_dec.c",
        "FreeImage/Source/LibWebP/src/dec/vp8_dec.c",
        "FreeImage/Source/LibWebP/src/dec/webp_dec.c",
        "FreeImage/Source/LibWebP/src/demux/anim_decode.c",
        "FreeImage/Source/LibWebP/src/demux/demux.c",
        "FreeImage/Source/LibWebP/src/dsp/alpha_processing.c",
        "FreeImage/Source/LibWebP/src/dsp/alpha_processing_mips_dsp_r2.c",
        "FreeImage/Source/LibWebP/src/dsp/alpha_processing_neon.c",
        "FreeImage/Source/LibWebP/src/dsp/alpha_processing_sse2.c",
        "FreeImage/Source/LibWebP/src/dsp/alpha_processing_sse41.c",
        "FreeImage/Source/LibWebP/src/dsp/cost.c",
        "FreeImage/Source/LibWebP/src/dsp/cost_mips32.c",
        "FreeImage/Source/LibWebP/src/dsp/cost_mips_dsp_r2.c",
        "FreeImage/Source/LibWebP/src/dsp/cost_sse2.c",
        "FreeImage/Source/LibWebP/src/dsp/cpu.c",
        "FreeImage/Source/LibWebP/src/dsp/dec.c",
        "FreeImage/Source/LibWebP/src/dsp/dec_clip_tables.c",
        "FreeImage/Source/LibWebP/src/dsp/dec_mips32.c",
        "FreeImage/Source/LibWebP/src/dsp/dec_mips_dsp_r2.c",
        "FreeImage/Source/LibWebP/src/dsp/dec_msa.c",
        "FreeImage/Source/LibWebP/src/dsp/dec_neon.c",
        "FreeImage/Source/LibWebP/src/dsp/dec_sse2.c",
        "FreeImage/Source/LibWebP/src/dsp/dec_sse41.c",
        "FreeImage/Source/LibWebP/src/dsp/enc.c",
        "FreeImage/Source/LibWebP/src/dsp/enc_avx2.c",
        "FreeImage/Source/LibWebP/src/dsp/enc_mips32.c",
        "FreeImage/Source/LibWebP/src/dsp/enc_mips_dsp_r2.c",
        "FreeImage/Source/LibWebP/src/dsp/enc_msa.c",
        "FreeImage/Source/LibWebP/src/dsp/enc_neon.c",
        "FreeImage/Source/LibWebP/src/dsp/enc_sse2.c",
        "FreeImage/Source/LibWebP/src/dsp/enc_sse41.c",
        "FreeImage/Source/LibWebP/src/dsp/filters.c",
        "FreeImage/Source/LibWebP/src/dsp/filters_mips_dsp_r2.c",
        "FreeImage/Source/LibWebP/src/dsp/filters_msa.c",
        "FreeImage/Source/LibWebP/src/dsp/filters_neon.c",
        "FreeImage/Source/LibWebP/src/dsp/filters_sse2.c",
        "FreeImage/Source/LibWebP/src/dsp/lossless.c",
        "FreeImage/Source/LibWebP/src/dsp/lossless_enc.c",
        "FreeImage/Source/LibWebP/src/dsp/lossless_enc_mips32.c",
        "FreeImage/Source/LibWebP/src/dsp/lossless_enc_mips_dsp_r2.c",
        "FreeImage/Source/LibWebP/src/dsp/lossless_enc_msa.c",
        "FreeImage/Source/LibWebP/src/dsp/lossless_enc_neon.c",
        "FreeImage/Source/LibWebP/src/dsp/lossless_enc_sse2.c",
        "FreeImage/Source/LibWebP/src/dsp/lossless_enc_sse41.c",
        "FreeImage/Source/LibWebP/src/dsp/lossless_mips_dsp_r2.c",
        "FreeImage/Source/LibWebP/src/dsp/lossless_msa.c",
        "FreeImage/Source/LibWebP/src/dsp/lossless_neon.c",
        "FreeImage/Source/LibWebP/src/dsp/lossless_sse2.c",
        "FreeImage/Source/LibWebP/src/dsp/rescaler.c",
        "FreeImage/Source/LibWebP/src/dsp/rescaler_mips32.c",
        "FreeImage/Source/LibWebP/src/dsp/rescaler_mips_dsp_r2.c",
        "FreeImage/Source/LibWebP/src/dsp/rescaler_msa.c",
        "FreeImage/Source/LibWebP/src/dsp/rescaler_neon.c",
        "FreeImage/Source/LibWebP/src/dsp/rescaler_sse2.c",
        "FreeImage/Source/LibWebP/src/dsp/ssim.c",
        "FreeImage/Source/LibWebP/src/dsp/ssim_sse2.c",
        "FreeImage/Source/LibWebP/src/dsp/upsampling.c",
        "FreeImage/Source/LibWebP/src/dsp/upsampling_mips_dsp_r2.c",
        "FreeImage/Source/LibWebP/src/dsp/upsampling_msa.c",
        "FreeImage/Source/LibWebP/src/dsp/upsampling_neon.c",
        "FreeImage/Source/LibWebP/src/dsp/upsampling_sse2.c",
        "FreeImage/Source/LibWebP/src/dsp/upsampling_sse41.c",
        "FreeImage/Source/LibWebP/src/dsp/yuv.c",
        "FreeImage/Source/LibWebP/src/dsp/yuv_mips32.c",
        "FreeImage/Source/LibWebP/src/dsp/yuv_mips_dsp_r2.c",
        "FreeImage/Source/LibWebP/src/dsp/yuv_neon.c",
        "FreeImage/Source/LibWebP/src/dsp/yuv_sse2.c",
        "FreeImage/Source/LibWebP/src/dsp/yuv_sse41.c",
        "FreeImage/Source/LibWebP/src/enc/alpha_enc.c",
        "FreeImage/Source/LibWebP/src/enc/analysis_enc.c",
        "FreeImage/Source/LibWebP/src/enc/backward_references_cost_enc.c",
        "FreeImage/Source/LibWebP/src/enc/backward_references_enc.c",
        "FreeImage/Source/LibWebP/src/enc/config_enc.c",
        "FreeImage/Source/LibWebP/src/enc/cost_enc.c",
        "FreeImage/Source/LibWebP/src/enc/filter_enc.c",
        "FreeImage/Source/LibWebP/src/enc/frame_enc.c",
        "FreeImage/Source/LibWebP/src/enc/histogram_enc.c",
        "FreeImage/Source/LibWebP/src/enc/iterator_enc.c",
        "FreeImage/Source/LibWebP/src/enc/near_lossless_enc.c",
        "FreeImage/Source/LibWebP/src/enc/picture_csp_enc.c",
        "FreeImage/Source/LibWebP/src/enc/picture_enc.c",
        "FreeImage/Source/LibWebP/src/enc/picture_psnr_enc.c",
        "FreeImage/Source/LibWebP/src/enc/picture_rescale_enc.c",
        "FreeImage/Source/LibWebP/src/enc/picture_tools_enc.c",
        "FreeImage/Source/LibWebP/src/enc/predictor_enc.c",
        "FreeImage/Source/LibWebP/src/enc/quant_enc.c",
        "FreeImage/Source/LibWebP/src/enc/syntax_enc.c",
        "FreeImage/Source/LibWebP/src/enc/token_enc.c",
        "FreeImage/Source/LibWebP/src/enc/tree_enc.c",
        "FreeImage/Source/LibWebP/src/enc/vp8l_enc.c",
        "FreeImage/Source/LibWebP/src/enc/webp_enc.c",
        "FreeImage/Source/LibWebP/src/mux/anim_encode.c",
        "FreeImage/Source/LibWebP/src/mux/muxedit.c",
        "FreeImage/Source/LibWebP/src/mux/muxinternal.c",
        "FreeImage/Source/LibWebP/src/mux/muxread.c",
        "FreeImage/Source/LibWebP/src/utils/bit_reader_utils.c",
        "FreeImage/Source/LibWebP/src/utils/bit_writer_utils.c",
        "FreeImage/Source/LibWebP/src/utils/color_cache_utils.c",
        "FreeImage/Source/LibWebP/src/utils/filters_utils.c",
        "FreeImage/Source/LibWebP/src/utils/huffman_encode_utils.c",
        "FreeImage/Source/LibWebP/src/utils/huffman_utils.c",
        "FreeImage/Source/LibWebP/src/utils/quant_levels_dec_utils.c",
        "FreeImage/Source/LibWebP/src/utils/quant_levels_utils.c",
        "FreeImage/Source/LibWebP/src/utils/random_utils.c",
        "FreeImage/Source/LibWebP/src/utils/rescaler_utils.c",
        "FreeImage/Source/LibWebP/src/utils/thread_utils.c",
        "FreeImage/Source/LibWebP/src/utils/utils.c",
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
    ],
    "include_dirs": [
        "FreeImage/Source",
        "FreeImage/Source/Metadata",
        "FreeImage/Source/FreeImageToolkit",
        "FreeImage/Source/LibJPEG",
        "FreeImage/Source/LibPNG",
        "FreeImage/Source/LibTIFF4",
        "FreeImage/Source/ZLib",
        "FreeImage/Source/LibOpenJPEG",
        "FreeImage/Source/OpenEXR",
        "FreeImage/Source/OpenEXR/Half",
        "FreeImage/Source/OpenEXR/Iex",
        "FreeImage/Source/OpenEXR/IlmImf",
        "FreeImage/Source/OpenEXR/IlmThread",
        "FreeImage/Source/OpenEXR/Imath",
        "FreeImage/Source/OpenEXR/IexMath",
        "FreeImage/Source/LibRawLite",
        "FreeImage/Source/LibRawLite/dcraw",
        "FreeImage/Source/LibRawLite/internal",
        "FreeImage/Source/LibRawLite/libraw",
        "FreeImage/Source/LibRawLite/src",
        "FreeImage/Source/LibWebP",
        "FreeImage/Source/LibJXR",
        "FreeImage/Source/LibJXR/common/include",
        "FreeImage/Source/LibJXR/image/sys",
        "FreeImage/Source/LibJXR/jxrgluelib",
    ],
    "macros": [
        ("OPJ_STATIC", None),
        ("DISABLE_PERF_MEASUREMENT", None),
        ("__ANSI__", None),
        ("NO_LCMS", None),
    ],
    "compiler_preargs": [
        "-O3",
        "-fPIC",
        "-fexceptions",
        "-fvisibility=hidden",
        "-Wno-ctor-dtor-privacy",
    ],
    "linker_preargs": [
        "-s",
        "-shared",
        "-Wl,-soname,libfreeimage.so",
    ],
    "linker_postargs": [
        "-lstdc++",
    ],
}
