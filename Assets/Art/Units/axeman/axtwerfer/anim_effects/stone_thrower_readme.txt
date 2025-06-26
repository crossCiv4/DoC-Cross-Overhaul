UNIT AND STONE THROWING MANAGEMENT

To manage this unit and the combat with stones during ranged animation sequence, you must:

1) edit your custom <Type>, <Button>, <NIF>, <KFM>, <SHADERNIF> and <TrainSound> parameters into the code below, and insert it into your CIV4ArtDefines_Unit.xml

		<UnitArtInfo>
			<Type>[...your define...]</Type>
			<Button>[...your button path...]</Button>
			<fScale>0.44</fScale>
			<fInterfaceScale>1.0</fInterfaceScale>
			<bActAsLand>0</bActAsLand>
			<bActAsAir>0</bActAsAir>
			<NIF>[...your path...]/troglodyte/stone_thrower.nif</NIF>
			<KFM>[...your path...]/troglodyte/anim/stone_thrower.kfm</KFM>
			<SHADERNIF>[...your path...]/troglodyte/stone_thrower_FX.nif</SHADERNIF>
			<ShadowDef>
				<ShadowNIF>Art/Units/01_UnitShadows/UnitShadow.nif</ShadowNIF>
				<ShadowAttachNode>BIP Pelvis</ShadowAttachNode>
				<fShadowScale>1.0</fShadowScale>
			</ShadowDef>
			<fBattleDistance>0.35</fBattleDistance>
			<fRangedDeathTime>0.31</fRangedDeathTime>
			<bActAsRanged>1</bActAsRanged>
			<TrainSound>[...your sound define...]</TrainSound>
			<AudioRunSounds>
				<AudioRunTypeLoop/>
				<AudioRunTypeEnd/>
			</AudioRunSounds>
		</UnitArtInfo>


2) append the following code into your CIV4EffectInfos.xml, editing the <Path> row below:

		<!-- stone bullets:-->
		<EffectInfo>
			<Type>EFFECT_STONE_BULLET</Type>
			<Description>Stone Bullet</Description>
			<fScale>1.0</fScale>
			<fUpdateRate>1.0</fUpdateRate>
			<Path>[...your path...]/troglodyte/anim_effects/stone_bullet.nif</Path>
			<bIsProjectile>1</bIsProjectile>
			<fSpeed>500.0</fSpeed>
			<fArcValue>2.0</fArcValue>
		</EffectInfo>
