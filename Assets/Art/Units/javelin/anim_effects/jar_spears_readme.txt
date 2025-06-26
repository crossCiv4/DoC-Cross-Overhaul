JAVELINES MANAGEMENT

If you wish to preserve the right kind of javelin during combat animation sequence, you must:

1) append the following code into your modded CIV4EffectInfos.xml, editing the <Path> rows below:

		<!--javelineer spears:-->
		<EffectInfo>
			<Type>EFFECT_MALISPEAR1</Type>
			<Description>Mali Spear</Description>
			<fScale>1.0</fScale>
			<fUpdateRate>1.0</fUpdateRate>
			<Path>[...your path...]/anim_effects/jav_spear1.nif</Path>
			<bIsProjectile>1</bIsProjectile>
			<fSpeed>500.0</fSpeed>
			<fArcValue>0.0</fArcValue>
		</EffectInfo>
		<EffectInfo>
			<Type>EFFECT_MALISPEAR2</Type>
			<Description>Mali Spear</Description>
			<fScale>1.0</fScale>
			<fUpdateRate>1.0</fUpdateRate>
			<Path>[...your path...]/anim_effects/jav_spear2.nif</Path>
			<bIsProjectile>1</bIsProjectile>
			<fSpeed>500.0</fSpeed>
			<fArcValue>0.0</fArcValue>
		</EffectInfo>

2) address the right kind of kfm into <KFM> rows of your modded CIV4ArtDefines_Unit.xml as follow:

for javelineers using light brown spears:
			<KFM>[...your path...]/anim_jar/javelineer_1.kfm</KFM>
 
for javelineers using dark brown spears:
			<KFM>[...your path...]/anim_jar/javelineer_2.kfm</KFM>
 
During combat sequence, each modified *_kfm calls its rangedstrik#.kf animation, each #.kf calls its EFFECT_XXX xml <Type>, each EFFECT_XXX calls its effect-nif properly.
 