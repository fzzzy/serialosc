{
	"patcher" : 	{
		"fileversion" : 1,
		"rect" : [ 134.0, 81.0, 626.0, 420.0 ],
		"bglocked" : 0,
		"defrect" : [ 134.0, 81.0, 626.0, 420.0 ],
		"openrect" : [ 0.0, 0.0, 0.0, 0.0 ],
		"openinpresentation" : 0,
		"default_fontsize" : 12.0,
		"default_fontface" : 0,
		"default_fontname" : "Andale Mono",
		"gridonopen" : 0,
		"gridsize" : [ 16.0, 16.0 ],
		"gridsnaponopen" : 0,
		"toolbarvisible" : 1,
		"boxanimatetime" : 200,
		"imprint" : 0,
		"enablehscroll" : 1,
		"enablevscroll" : 1,
		"boxes" : [ 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "loadmess browse",
					"numinlets" : 1,
					"numoutlets" : 1,
					"id" : "obj-14",
					"fontname" : "Andale Mono",
					"outlettype" : [ "" ],
					"patching_rect" : [ 64.0, 96.0, 119.0, 20.0 ],
					"fontsize" : 12.0
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "message",
					"text" : "/sys/port 8001",
					"numinlets" : 2,
					"numoutlets" : 1,
					"id" : "obj-11",
					"fontname" : "Andale Mono",
					"outlettype" : [ "" ],
					"patching_rect" : [ 240.0, 272.0, 111.0, 18.0 ],
					"fontsize" : 12.0
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "t b s",
					"numinlets" : 1,
					"numoutlets" : 2,
					"id" : "obj-9",
					"fontname" : "Andale Mono",
					"outlettype" : [ "bang", "" ],
					"patching_rect" : [ 304.0, 240.0, 47.0, 20.0 ],
					"fontsize" : 12.0
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "prepend resolve",
					"numinlets" : 1,
					"numoutlets" : 1,
					"id" : "obj-8",
					"fontname" : "Andale Mono",
					"outlettype" : [ "" ],
					"patching_rect" : [ 208.0, 160.0, 119.0, 20.0 ],
					"fontsize" : 12.0
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "umenu",
					"items" : "serialosc/m64-0000",
					"numinlets" : 1,
					"numoutlets" : 3,
					"id" : "obj-7",
					"fontname" : "Andale Mono",
					"outlettype" : [ "int", "", "" ],
					"types" : [  ],
					"patching_rect" : [ 208.0, 128.0, 166.0, 20.0 ],
					"fontsize" : 12.0
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "oscbonjour",
					"numinlets" : 1,
					"numoutlets" : 3,
					"id" : "obj-6",
					"fontname" : "Andale Mono",
					"outlettype" : [ "", "", "" ],
					"patching_rect" : [ 64.0, 128.0, 83.0, 20.0 ],
					"fontsize" : 12.0
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "udpsend localhost 9999",
					"numinlets" : 1,
					"numoutlets" : 0,
					"id" : "obj-5",
					"fontname" : "Andale Mono",
					"patching_rect" : [ 384.0, 304.0, 169.0, 20.0 ],
					"fontsize" : 12.0
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "prepend /led",
					"numinlets" : 1,
					"numoutlets" : 1,
					"id" : "obj-4",
					"fontname" : "Andale Mono",
					"outlettype" : [ "" ],
					"patching_rect" : [ 384.0, 272.0, 97.0, 20.0 ],
					"fontsize" : 12.0
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "matrixctrl",
					"numinlets" : 1,
					"presentation_rect" : [ 0.0, 0.0, 130.0, 128.0 ],
					"numoutlets" : 2,
					"id" : "obj-3",
					"outlettype" : [ "list", "list" ],
					"rows" : 8,
					"patching_rect" : [ 384.0, 128.0, 130.0, 130.0 ],
					"autosize" : 1
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "route /press",
					"numinlets" : 1,
					"numoutlets" : 2,
					"id" : "obj-2",
					"fontname" : "Andale Mono",
					"outlettype" : [ "", "" ],
					"patching_rect" : [ 384.0, 96.0, 97.0, 20.0 ],
					"fontsize" : 12.0
				}

			}
, 			{
				"box" : 				{
					"maxclass" : "newobj",
					"text" : "udpreceive 8001",
					"numinlets" : 1,
					"numoutlets" : 1,
					"id" : "obj-1",
					"fontname" : "Andale Mono",
					"outlettype" : [ "" ],
					"patching_rect" : [ 384.0, 64.0, 119.0, 20.0 ],
					"fontsize" : 12.0
				}

			}
 ],
		"lines" : [ 			{
				"patchline" : 				{
					"source" : [ "obj-1", 0 ],
					"destination" : [ "obj-2", 0 ],
					"hidden" : 0,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-2", 0 ],
					"destination" : [ "obj-3", 0 ],
					"hidden" : 0,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-3", 0 ],
					"destination" : [ "obj-4", 0 ],
					"hidden" : 0,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-4", 0 ],
					"destination" : [ "obj-5", 0 ],
					"hidden" : 0,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-6", 2 ],
					"destination" : [ "obj-7", 0 ],
					"hidden" : 0,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-7", 1 ],
					"destination" : [ "obj-8", 0 ],
					"hidden" : 0,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-8", 0 ],
					"destination" : [ "obj-6", 0 ],
					"hidden" : 0,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-6", 0 ],
					"destination" : [ "obj-9", 0 ],
					"hidden" : 0,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-9", 0 ],
					"destination" : [ "obj-11", 0 ],
					"hidden" : 0,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-9", 1 ],
					"destination" : [ "obj-5", 0 ],
					"hidden" : 0,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-11", 0 ],
					"destination" : [ "obj-5", 0 ],
					"hidden" : 0,
					"midpoints" : [  ]
				}

			}
, 			{
				"patchline" : 				{
					"source" : [ "obj-14", 0 ],
					"destination" : [ "obj-6", 0 ],
					"hidden" : 0,
					"midpoints" : [  ]
				}

			}
 ]
	}

}
